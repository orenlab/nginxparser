import re

log_pattern = re.compile(
    r'(?P<ip>\S+) - - \[(?P<date>[^]]+)] "(?P<method>\S*) ?(?P<request>[^ ]*) ?HTTP/\d*\.\d*" (?P<status>\d+) \d+ "(?P<referrer>[^"]*)" "(?P<user_agent>[^"]*)"'
)

# Patterns for identifying potential threats and their severity levels
danger_patterns = {
    "SQL Injection": (r"(?i)\b(SELECT|UNION|INSERT|UPDATE|DELETE|DROP|ALTER)\b", "High"),
    "XSS": (r"(?i)<script\b[^<]*(?:(?!<\/script>)<[^<]*)*<\/script>", "High"),
    "Critical File Access": (r"/(\.env|\.git/config|/etc/passwd)", "Medium"),
    "Filter Bypass": (r"%2e%2e|%252e|%5c%5c", "Low"),
    "Shell Access": (r"/(bin/sh|cmd\.exe)", "High"),
    "CGI Access": (r"/cgi-bin/[^ ]*", "High"),
    "PHP Access": (r"\.php\b", "High"),
    "Python Access": (r"\.py\b", "High"),
    "Directory Access": (r"/(\.\.|/\\)", "High"),
    "Empty Request": (r"^\s*$", "Low")
}
