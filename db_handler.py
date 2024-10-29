import sqlite3
from collections import defaultdict
from logger import logging


def connect_to_database(db_name: str = "blocked_ips.db") -> sqlite3.Connection:
    """Connects to the SQLite database and returns the connection."""
    return sqlite3.connect(db_name)


def setup_database(conn: sqlite3.Connection):
    """Sets up the SQLite3 database and creates necessary tables."""
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS blocked_ips (
            ip TEXT PRIMARY KEY,
            reason TEXT,
            blocked_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    return conn


def log_blocked_ip(conn: sqlite3.Connection, ip: str, reason: str):
    """Logs the blocked IP in the database."""
    cursor = conn.cursor()
    cursor.execute('''
        INSERT OR REPLACE INTO blocked_ips (ip, reason)
        VALUES (?, ?)
    ''', (ip, reason))
    conn.commit()
    logging.info(f"Logged blocked IP: {ip} | Reason: {reason}")


def is_ip_blocked(conn: sqlite3.Connection, ip: str) -> bool:
    """Checks if the IP is already blocked in the database."""
    cursor = conn.cursor()
    cursor.execute('SELECT COUNT(*) FROM blocked_ips WHERE ip = ?', (ip,))
    count = cursor.fetchone()[0]
    return count > 0


def generate_report(conn: sqlite3.Connection):
    """Generates a report of blocked IPs by reason."""
    cursor = conn.cursor()
    cursor.execute('SELECT ip, reason FROM blocked_ips')
    rows = cursor.fetchall()

    report = defaultdict(list)
    for ip, reason in rows:
        report[reason].append(ip)

    print("\n--- Blocked IPs Report ---")
    for reason, ips in report.items():
        print(f"\nReason: {reason}")
        for ip in ips:
            print(f"  - {ip}")
    print("\n--------------------------")
