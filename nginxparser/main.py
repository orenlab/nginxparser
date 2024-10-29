import re
import json
import subprocess
import argparse
from collections import defaultdict, Counter
from typing import List, Dict, Any
import ipaddress
from nginxparser import db_handler
from logger import logging
import patterns


def is_valid_ip(ip: str) -> bool:
    """Checks if the provided IP is a valid IPv4 or IPv6 address."""
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False


def parse_log_line(line: str) -> tuple[str | Any, str | Any, int, str | Any] | tuple[None, None, None, None]:
    """Parses a single line of the Nginx log and returns relevant fields, including empty requests."""

    match = patterns.log_pattern.match(line)
    if match:
        ip = match.group("ip")
        method = match.group("method")
        request = match.group("request")
        status = int(match.group("status"))
        user_agent = match.group("user_agent")

        # Check if the request is empty (missing method or request URI)
        if not method or not request:
            return ip, "Empty Request", status, user_agent

        return ip, request, status, user_agent

    return None, None, None, None


def analyze_logs(log_lines: List[str]) -> Dict:
    """Analyzes log lines and returns a structured dictionary of data for analysis."""
    errors = defaultdict(lambda: defaultdict(list))
    ip_hit_counts = Counter()
    request_patterns = Counter()
    threat_analysis = []
    firewall_rules = []

    for line in log_lines:
        ip, request, status, user_agent = parse_log_line(line)
        if ip and request and status in {400, 403, 404, 405, 503}:
            errors[status][ip].append(request)
            ip_hit_counts[ip] += 1
            request_patterns[request] += 1

            # Check each request for potential threats and add to threat analysis
            for threat_name, (pattern, severity) in patterns.danger_patterns.items():
                if re.search(pattern, request):
                    threat_analysis.append({
                        "ip": ip,
                        "request": request,
                        "threat_type": threat_name,
                        "severity": severity
                    })
                    # Add to firewall rules if severity is high or medium
                    if severity in {"High", "Medium"}:
                        firewall_rules.append({
                            "ip": ip,
                            "rule": f"ufw deny from {ip} # Blocked due to {threat_name} pattern",
                            "reason": threat_name
                        })

    unique_ips_count = len(ip_hit_counts)
    total_hits = sum(ip_hit_counts.values())

    # Alphabetically sorted request patterns with counts
    sorted_request_patterns = sorted(request_patterns.items())

    # Formatting results in JSON structure
    results = {
        "error_summary": {
            error_code: [
                {"ip": ip, "requests": list(set(requests))}
                for ip, requests in ip_requests.items()
            ]
            for error_code, ip_requests in errors.items()
        },
        "ip_hit_statistics": {
            "unique_ips": unique_ips_count,
            "total_hits": total_hits
        },
        "sorted_request_patterns": [
            {"request": request, "count": count}
            for request, count in sorted_request_patterns
        ],
        "firewall_rules": firewall_rules,
        "threat_analysis": threat_analysis
    }

    return results


def block_ips(firewall_rules: List[Dict[str, str]], conn: db_handler.sqlite3.Connection):
    """Blocks unique, valid IPs in ufw with a deny rule and logs the action."""
    unique_ips = set(rule["ip"] for rule in firewall_rules if is_valid_ip(rule["ip"]))  # Filter unique valid IPs

    for ip in unique_ips:
        if db_handler.is_ip_blocked(conn, ip):
            logging.warning(f"IP {ip} is already blocked. Skipping...")
            continue

        # Retrieve the reason for blocking from the first matching rule in the firewall_rules list
        reason = next(rule["reason"] for rule in firewall_rules if rule["ip"] == ip)

        try:
            command = ["ufw", "deny", "from", ip, "to", "any", "comment", f"Blocked due to {reason}"]
            subprocess.run(command, check=True)
            logging.info(f"Blocked IP: {ip} | Reason: {reason}")
            db_handler.log_blocked_ip(conn, ip, reason)
        except subprocess.CalledProcessError as e:
            logging.error(f"Failed to block IP {ip}: {e}")


def test_log_format(log_lines: List[str]):
    """Tests the last two log entries against the expected log pattern."""
    # Take the last two log entries
    last_two_entries = log_lines[-2:]

    print("\n--- Testing Log Format ---")
    for idx, line in enumerate(last_two_entries, start=1):
        ip, request, status, user_agent = parse_log_line(line)
        if ip and request and status and user_agent:
            print(f"Entry {idx} matches expected format:")
            print(f"  IP: {ip}")
            print(f"  Request: {request}")
            print(f"  Status: {status}")
            print(f"  User-Agent: {user_agent}")
        else:
            print(f"Entry {idx} does not match the expected format or has missing values.")
    print("--- Test Complete ---\n")


def main():
    """Main function to parse arguments, analyze logs, and optionally block IPs."""
    parser = argparse.ArgumentParser(description="Analyze Nginx logs and optionally block IPs with high error rates.")
    parser.add_argument("-p", "--path", default="/var/log/nginx/access.log", help="Path to the Nginx log file")
    parser.add_argument("--info", action="store_true", help="Display log analysis information only")
    parser.add_argument("--block", action="store_true", help="Block IPs with high error rates using ufw")
    parser.add_argument("--report", action="store_true", help="Generate a report of blocked IPs by reason")
    parser.add_argument("--test-format", action="store_true", help="Test the format of the last two log entries")
    args = parser.parse_args()

    # Check for ufw
    if not check_ufw():
        logging.error("UFW is not available or not accessible. Exiting.")
        exit(1)

    # Read logs
    try:
        with open(args.path, 'r') as log_file:
            log_lines = log_file.readlines()

        if args.test_format:
            test_log_format(log_lines)
            return

        analysis_results = analyze_logs(log_lines)

        # Set up database
        conn = db_handler.connect_to_database()
        db_handler.setup_database(conn)

        if args.info:
            # Display analysis information only
            logging.info(json.dumps(analysis_results, indent=4))
        elif args.block:
            # Display and execute blocking of IPs
            firewall_rules = analysis_results["firewall_rules"]
            if firewall_rules:
                logging.info("Blocking the following IPs:")
                block_ips(firewall_rules, conn)
            else:
                logging.info("No IPs to block.")
        elif args.report:
            # Generate a report of blocked IPs
            db_handler.generate_report(conn)
        else:
            logging.error(
                "Please specify --info to display information, --block to block IPs, or --report to generate a report.")

        conn.close()

    except FileNotFoundError:
        logging.error(f"Log file not found: {args.path}")
    except Exception as e:
        logging.error(f"An error occurred: {e}")


def check_ufw() -> bool:
    """Checks if UFW is installed and accessible."""
    try:
        subprocess.run(["ufw", "status"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False


if __name__ == "__main__":
    main()
