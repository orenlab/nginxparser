import re

log_pattern = re.compile(
    r'(?P<ip>\S+) - - \[(?P<date>[^]]+)] "(?P<method>\S*) ?(?P<request>[^ ]*) ?HTTP/\d*\.\d*" (?P<status>\d+) \d+ "(?P<referrer>[^"]*)" "(?P<user_agent>[^"]*)"'
)

# Patterns for identifying potential threats and their severity levels
danger_patterns = {
    # SQL Injection: Checks for SQL keywords like SELECT, UNION, INSERT, etc., which are often used in SQL injection attacks to retrieve or manipulate database data.
    "SQL Injection": (r"(?i)\b(SELECT|UNION|INSERT|UPDATE|DELETE|DROP|ALTER)\b", "High"),

    # XSS (Cross-Site Scripting): Searches for <script> tags that are commonly used in XSS attacks to inject malicious JavaScript code into web pages.
    "XSS": (r"(?i)<script\b[^<]*(?:(?!<\/script>)<[^<]*)*<\/script>", "High"),

    # Critical File Access: Attempts to access critical files like .env, .git/config, and /etc/passwd, which may contain sensitive configurations or credentials.
    "Critical File Access": (r"/(\.env|\.git/config|/etc/passwd)", "Medium"),

    # Filter Bypass: Detects encoding tricks like %2e%2e or %5c%5c that may indicate attempts to bypass security filters.
    "Filter Bypass": (r"%2e%2e|%252e|%5c%5c", "Low"),

    # Shell Access: Checks for access to shell commands like bin/sh or cmd.exe, which could indicate attempts to execute system commands.
    "Shell Access": (r"/(bin/sh|cmd\.exe)", "High"),

    # CGI Access: Scans for requests to CGI scripts, which are often vulnerable to exploits. CGI directories can contain vulnerable scripts.
    "CGI Access": (r"/cgi-bin/[^ ]*", "High"),

    # PHP Access: Accessing PHP scripts may signal attempts to exploit vulnerabilities within those scripts.
    "PHP Access": (r"\.php\b", "High"),

    # Python Access: Requests for .py files may indicate probing for Python scripts, which can expose application internals or sensitive data.
    "Python Access": (r"\.py\b", "High"),

    # Directory Access: Detects traversal patterns like /../ or /\ that can be used to navigate out of restricted directories.
    "Directory Access": (r"/(\.\.|/\\)", "High"),

    # Empty Request: Empty requests might indicate poorly configured automated scanners or tools probing the server.
    "Empty Request": (r"^\s*$", "Low"),

    # Invalid SSL Handshake: Detects invalid SSL handshake bytes (e.g., \\x16\\x03\\x01), possibly indicating a misconfigured client or malicious probing.
    "Invalid SSL Handshake": (r"\\x16\\x03\\x01", "Medium"),

    # Empty User-Agent: An empty User-Agent may suggest a bot or a poorly configured scanning tool.
    "Empty User-Agent": (r'"-" "-"$', "Low"),

    # Unusual Method: Detects uncommon HTTP methods like PRI * or SSTP_DUPLEX_POST that may indicate probing or misconfigured clients.
    "Unusual Method": (r"(PRI \*|SSTP_DUPLEX_POST)", "Medium"),

    # Miner Requests: Looks for requests related to cryptocurrency mining (e.g., mining pools, XMRig), which could indicate unauthorized mining activity.
    "Miner Requests": (r"\b(mining\.\w+|eth_submitLogin|XMRig)\b", "High"),

    # Unusual Encoding: Checks for unusual encoding sequences (like %2e%2e or %25), often used to obfuscate attacks or bypass filters.
    "Unusual Encoding": (r"%2e%2e|%2e|%25|%00", "Medium"),

    # Potential Scanner: Detects common scanner and automation tool User-Agents like zgrab, Keydrop, Go, curl, wget, and CensysInspect, indicating potential scanning activity.
    "Potential Scanner": (r"(zgrab|Keydrop|Go|curl|wget|Hello World|CensysInspect)", "Medium")
}
