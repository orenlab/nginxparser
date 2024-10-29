## PythonNginxParser 🚀

PythonNginxParser is a robust and highly configurable tool for analyzing and securing Nginx server logs. It enables
proactive identification of threats and blocking of malicious IPs, helping to safeguard your server and ensure smooth
operation. Built with modularity and performance in mind, PythonNginxParser is designed to scale with your needs and
adapt
to evolving security challenges.

## Features 🌟

- Advanced Log Errors Parsing: Supports both IPv4 and IPv6, and handles empty requests.
- Threat Detection: Identifies common threats, such as SQL Injection, XSS, file access attempts, and CGI-bin exploits.
- Automated IP Blocking: Integrates with UFW to block malicious IPs based on customizable threat patterns.
- Daily Telegram Reports: Summarizes key events and insights from the previous day’s logs, with emojis for readability.
- SQLite3 Logging: Stores blocked IPs and their associated reasons in an SQLite3 database.
- Modular Design: Each major functionality is encapsulated in separate modules for easy maintenance and scaling.

## Project Structure 📁

- `db_handler.py` - Handles all database interactions for storing and retrieving blocked IPs.
- `logger.py` - Configures and manages logging across all modules.
- `main.py` - Main execution script for log analysis, IP blocking, and reporting.
- `patterns.py` - Contains regex patterns and severity levels for threat detection.

## Requirements 📦

- Python 3.12+ (https://www.python.org/downloads/)
- Nginx (https://nginx.org/en/download.html)
- UFW (for firewall management) (https://ufw.readthedocs.io/en/latest/)
- SQLite3 (for logging blocked IPs) (https://www.sqlite.org/)

## Usage 🛠️

### Run PythonNginxParser with the following commands:

```bash
python main.py --path <path_to_nginx_log> --info
```

### Command-line Options

- `--info`: Display analysis information only.
- `--block`: Block IPs with high error rates using UFW.
- `--report`: Generate a report of blocked IPs by reason.
- `--test-format`: Test the format of the last two log entries.

Sample output can be found in the [sample_output.md](docs/sample_output.md) file.

### Example:

```bash
python main.py --path /var/log/nginx/access.log --block
```

## Configuration ⚙️

Customize patterns and severities in `patterns.py` to adjust threat detection criteria.

## Logging 📑

Logs are stored in `nginxparser.log`, capturing key events and actions for easy debugging and monitoring.

## Security Considerations 🔒

Ensure UFW and other system-level permissions are properly configured to prevent unauthorized access.

## Daily Telegram Reports 📱

Configure and receive daily summaries of threats detected in your Nginx logs. Enable this feature to stay informed on
critical issues without manually reviewing logs.

## Contributing 🤝

Contributions are welcome! Please fork the repository, make your changes, and submit a pull request. Follow our coding
guidelines and ensure all tests pass.

## License 📄

This project is licensed under the MIT License - see the LICENSE file for details.


