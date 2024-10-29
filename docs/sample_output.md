## Sample Output:

### The `--report` argument:

```bash
➜  nginxparser git:(main) ✗ python ./main.py --report
2024-10-29 18:28:38,765 - INFO - Connected to database: blocked_ips.db
2024-10-29 18:28:38,766 - INFO - Database setup completed.

--- Blocked IPs Report ---

Reason: Critical File Access
  - 142.93.1.91
  - 45.58.159.164

Reason: CGI Access
  - 185.224.128.83
  - 5.181.190.29

Reason: PHP Access
  - 208.110.70.42
  - 72.46.130.218

Reason: Shell Access
  - 143.244.150.76
  - 36.139.217.213

--------------------------
➜  nginxparser git:(main) ✗
```

### The `--block` argument:

```bash
➜  nginxparser git:(main) ✗ python ./main.py --block
2024-10-29 18:28:38,765 - INFO - Connected to database: blocked_ips.db
2024-10-29 18:28:38,766 - INFO - Database setup completed.
2024-10-29 18:28:06,833 - INFO - Blocked IP: 165.227.11.55 | Reason: Critical File Access
2024-10-29 18:28:06,836 - INFO - Logged blocked IP: 165.227.11.55 | Reason: Critical File Access
Rule updated
...
```

### The `--test-format` argument:

```bash
➜  nginxparser git:(main) ✗ python ./main.py --test-format

--- Testing Log Format ---
Entry 1 matches expected format:
  IP: 00.000.00.00
  Request: /
  Status: 200
  User-Agent: Mozilla/5.0 (Linux; Android 9; Pixel 2 XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.89 Mobile Safari/537.36
Entry 2 matches expected format:
  IP: 00.000.00.00
  Request: /
  Status: 200
  User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36
--- Test Complete ---

➜  nginxparser git:(main) ✗ 
```

### The `--info` argument:

```bash
➜  nginxparser git:(main) ✗ python ./main.py --info       
2024-10-29 18:41:48,982 - INFO - Connected to database: blocked_ips.db
2024-10-29 18:41:48,983 - INFO - Database setup completed.
2024-10-29 18:41:48,984 - INFO - {
    "error_summary": {
        "404": [
            {
                "ip": "164.52.24.188",
                "requests": [
                    "/favicon.ico"
                ]
            },
            {
                "ip": "208.110.70.42",
                "requests": [
                    "/restore.php"
                ]
            },
            {
                "ip": "178.215.238.67",
                "requests": [
                    "/login.rsp"
                ]
            },
            {
                "ip": "185.16.38.232",
                "requests": [
                    "/cgi-bin/luci/;stok=/locale"
                ]
            },
            {
                "ip": "80.75.212.46",
                "requests": [
                    "/login.rsp"
                ]
            }
        ],
        "403": [
            {
                "ip": "208.110.70.42",
                "requests": [
                    "/restore.php"
                ]
            },
            {
                "ip": "185.224.128.83",
                "requests": [
                    "/cgi-bin/luci/;stok=/locale"
                ]
            },
            {
                "ip": "45.148.10.172",
                "requests": [
                    "/.env"
                ]
            },
            {
                "ip": "45.148.10.206",
                "requests": [
                    "/.git/config"
                ]
            },
            {
                "ip": "146.190.63.48",
                "requests": [
                    "/.git/config",
                    "/.env"
                ]
            },
            {
                "ip": "159.89.47.107",
                "requests": [
                    "/.env"
                ]
            }
        ],
        "400": [
            {
                "ip": "209.38.153.122",
                "requests": [
                    "/t4",
                    "/"
                ]
            },
            {
                "ip": "13.64.193.92",
                "requests": [
                    "/"
                ]
            },
            {
                "ip": "165.227.11.55",
                "requests": [
                    "/.env"
                ]
            },
            {
                "ip": "143.244.150.76",
                "requests": [
                    "/cgi-bin/%%32%65%%32%65/%%32%65%%32%65/%%32%65%%32%65/%%32%65%%32%65/%%32%65%%32%65/%%32%65%%32%65/%%32%65%%32%65/bin/sh",
                    "/cgi-bin/.%2e/.%2e/.%2e/.%2e/.%2e/.%2e/.%2e/.%2e/.%2e/.%2e/bin/sh"
                ]
            },
            {
                "ip": "162.142.125.209",
                "requests": [
                    "*"
                ]
            },
            {
                "ip": "36.139.217.213",
                "requests": [
                    "/cgi-bin/%%32%65%%32%65/%%32%65%%32%65/%%32%65%%32%65/%%32%65%%32%65/%%32%65%%32%65/%%32%65%%32%65/%%32%65%%32%65/bin/sh",
                    "/cgi-bin/.%2e/.%2e/.%2e/.%2e/.%2e/.%2e/.%2e/.%2e/.%2e/.%2e/bin/sh"
                ]
            },
            {
                "ip": "72.46.130.218",
                "requests": [
                    "/admin/modules/framework/amp_conf/htdocs/admin/config.php"
                ]
            },
            {
                "ip": "45.58.159.164",
                "requests": [
                    "/.env"
                ]
            },
            {
                "ip": "66.132.153.61",
                "requests": [
                    "*"
                ]
            }
        ]
    },
    "ip_hit_statistics": {
        "unique_ips": 35,
        "total_hits": 76
    },
    "sorted_request_patterns": [
        {
            "request": "*",
            "count": 2
        },
        {
            "request": "/",
            "count": 2
        },
        {
            "request": "/.env",
            "count": 12
        },
        {
            "request": "/.git/config",
            "count": 3
        },
        {
            "request": "/admin/modules/framework/amp_conf/htdocs/admin/config.php",
            "count": 1
        },
        {
            "request": "/boaform/admin/formLogin",
            "count": 1
        },
        {
            "request": "/cgi-bin/%%32%65%%32%65/%%32%65%%32%65/%%32%65%%32%65/%%32%65%%32%65/%%32%65%%32%65/%%32%65%%32%65/%%32%65%%32%65/bin/sh",
            "count": 2
        },
        {
            "request": "/cgi-bin/.%2e/.%2e/.%2e/.%2e/.%2e/.%2e/.%2e/.%2e/.%2e/.%2e/bin/sh",
            "count": 2
        },
        {
            "request": "/cgi-bin/luci/;stok=/locale",
            "count": 11
        },
        {
            "request": "/favicon.ico",
            "count": 8
        },
        {
            "request": "/geoserver/web/",
            "count": 1
        },
        {
            "request": "/hello.world?%ADd+allow_url_include%3d1+%ADd+auto_prepend_file%3dphp://input",
            "count": 1
        },
        {
            "request": "/hudson",
            "count": 1
        },
        {
            "request": "/login.rsp",
            "count": 7
        },
        {
            "request": "/restore.php",
            "count": 12
        },
        {
            "request": "/restore.php?lang=en",
            "count": 4
        },
        {
            "request": "/slt",
            "count": 1
        },
        {
            "request": "/swt",
            "count": 1
        },
        {
            "request": "/t4",
            "count": 1
        },
        {
            "request": "/v1/dfapi/add",
            "count": 1
        },
        {
            "request": "/webui/",
            "count": 1
        },
        {
            "request": "/wp-login.php",
            "count": 1
        }
    ],
    "firewall_rules": [
        {
            "ip": "185.224.128.83",
            "rule": "ufw deny from 185.224.128.83 # Blocked due to CGI Access pattern",
            "reason": "CGI Access"
        },
        {
            "ip": "185.224.128.83",
            "rule": "ufw deny from 185.224.128.83 # Blocked due to CGI Access pattern",
            "reason": "CGI Access"
        },
        {
            "ip": "208.110.70.42",
            "rule": "ufw deny from 208.110.70.42 # Blocked due to PHP Access pattern",
            "reason": "PHP Access"
        },
        {
            "ip": "208.110.70.42",
            "rule": "ufw deny from 208.110.70.42 # Blocked due to PHP Access pattern",
            "reason": "PHP Access"
        },
        {
            "ip": "92.205.24.168",
            "rule": "ufw deny from 92.205.24.168 # Blocked due to PHP Access pattern",
            "reason": "PHP Access"
        },
        {
            "ip": "165.227.11.55",
            "rule": "ufw deny from 165.227.11.55 # Blocked due to Critical File Access pattern",
            "reason": "Critical File Access"
        },
        {
            "ip": "87.120.113.77",
            "rule": "ufw deny from 87.120.113.77 # Blocked due to Critical File Access pattern",
            "reason": "Critical File Access"
        },
        {
            "ip": "45.148.10.172",
            "rule": "ufw deny from 45.148.10.172 # Blocked due to Critical File Access pattern",
            "reason": "Critical File Access"
        },
        {
            "ip": "143.244.150.76",
            "rule": "ufw deny from 143.244.150.76 # Blocked due to Shell Access pattern",
            "reason": "Shell Access"
        },
        {
            "ip": "143.244.150.76",
            "rule": "ufw deny from 143.244.150.76 # Blocked due to CGI Access pattern",
            "reason": "CGI Access"
        },
        {
            "ip": "143.244.150.76",
            "rule": "ufw deny from 143.244.150.76 # Blocked due to Shell Access pattern",
            "reason": "Shell Access"
        },
        {
            "ip": "143.244.150.76",
            "rule": "ufw deny from 143.244.150.76 # Blocked due to CGI Access pattern",
            "reason": "CGI Access"
        },
        {
            "ip": "5.188.150.73",
            "rule": "ufw deny from 5.188.150.73 # Blocked due to PHP Access pattern",
            "reason": "PHP Access"
        },
        {
            "ip": "208.110.70.42",
            "rule": "ufw deny from 208.110.70.42 # Blocked due to PHP Access pattern",
            "reason": "PHP Access"
        },
        {
            "ip": "208.110.70.42",
            "rule": "ufw deny from 208.110.70.42 # Blocked due to PHP Access pattern",
            "reason": "PHP Access"
        },
        {
            "ip": "185.224.128.83",
            "rule": "ufw deny from 185.224.128.83 # Blocked due to CGI Access pattern",
            "reason": "CGI Access"
        },
        {
            "ip": "185.224.128.83",
            "rule": "ufw deny from 185.224.128.83 # Blocked due to CGI Access pattern",
            "reason": "CGI Access"
        },
        {
            "ip": "5.181.190.29",
            "rule": "ufw deny from 5.181.190.29 # Blocked due to CGI Access pattern",
            "reason": "CGI Access"
        },
        {
            "ip": "45.148.10.206",
            "rule": "ufw deny from 45.148.10.206 # Blocked due to Critical File Access pattern",
            "reason": "Critical File Access"
        },
        {
            "ip": "36.139.217.213",
            "rule": "ufw deny from 36.139.217.213 # Blocked due to Shell Access pattern",
            "reason": "Shell Access"
        },
        {
            "ip": "36.139.217.213",
            "rule": "ufw deny from 36.139.217.213 # Blocked due to CGI Access pattern",
            "reason": "CGI Access"
        },
        {
            "ip": "36.139.217.213",
            "rule": "ufw deny from 36.139.217.213 # Blocked due to Shell Access pattern",
            "reason": "Shell Access"
        },
        {
            "ip": "36.139.217.213",
            "rule": "ufw deny from 36.139.217.213 # Blocked due to CGI Access pattern",
            "reason": "CGI Access"
        },
        {
            "ip": "208.110.70.42",
            "rule": "ufw deny from 208.110.70.42 # Blocked due to PHP Access pattern",
            "reason": "PHP Access"
        },
        {
            "ip": "208.110.70.42",
            "rule": "ufw deny from 208.110.70.42 # Blocked due to PHP Access pattern",
            "reason": "PHP Access"
        },
        {
            "ip": "185.16.38.232",
            "rule": "ufw deny from 185.16.38.232 # Blocked due to CGI Access pattern",
            "reason": "CGI Access"
        },
        {
            "ip": "72.46.130.218",
            "rule": "ufw deny from 72.46.130.218 # Blocked due to PHP Access pattern",
            "reason": "PHP Access"
        },
        {
            "ip": "45.148.10.206",
            "rule": "ufw deny from 45.148.10.206 # Blocked due to Critical File Access pattern",
            "reason": "Critical File Access"
        },
        {
            "ip": "45.148.10.172",
            "rule": "ufw deny from 45.148.10.172 # Blocked due to Critical File Access pattern",
            "reason": "Critical File Access"
        },
        {
            "ip": "185.224.128.83",
            "rule": "ufw deny from 185.224.128.83 # Blocked due to CGI Access pattern",
            "reason": "CGI Access"
        }
    ],
    "threat_analysis": [
        {
            "ip": "208.110.70.42",
            "request": "/restore.php",
            "threat_type": "PHP Access",
            "severity": "High"
        },
        {
            "ip": "208.110.70.42",
            "request": "/restore.php",
            "threat_type": "PHP Access",
            "severity": "High"
        },
        {
            "ip": "185.16.38.232",
            "request": "/cgi-bin/luci/;stok=/locale",
            "threat_type": "CGI Access",
            "severity": "High"
        },
        {
            "ip": "185.224.128.83",
            "request": "/cgi-bin/luci/;stok=/locale",
            "threat_type": "CGI Access",
            "severity": "High"
        },
        {
            "ip": "185.224.128.83",
            "request": "/cgi-bin/luci/;stok=/locale",
            "threat_type": "CGI Access",
            "severity": "High"
        },
        {
            "ip": "208.110.70.42",
            "request": "/restore.php",
            "threat_type": "PHP Access",
            "severity": "High"
        },
        {
            "ip": "208.110.70.42",
            "request": "/restore.php",
            "threat_type": "PHP Access",
            "severity": "High"
        },
        {
            "ip": "92.205.24.168",
            "request": "/restore.php?lang=en",
            "threat_type": "PHP Access",
            "severity": "High"
        },
        {
            "ip": "165.227.11.55",
            "request": "/.env",
            "threat_type": "Critical File Access",
            "severity": "Medium"
        },
        {
            "ip": "87.120.113.77",
            "request": "/.env",
            "threat_type": "Critical File Access",
            "severity": "Medium"
        },
        {
            "ip": "45.148.10.172",
            "request": "/.env",
            "threat_type": "Critical File Access",
            "severity": "Medium"
        },
        {
            "ip": "143.244.150.76",
            "request": "/cgi-bin/.%2e/.%2e/.%2e/.%2e/.%2e/.%2e/.%2e/.%2e/.%2e/.%2e/bin/sh",
            "threat_type": "Shell Access",
            "severity": "High"
        },
        {
            "ip": "143.244.150.76",
            "request": "/cgi-bin/.%2e/.%2e/.%2e/.%2e/.%2e/.%2e/.%2e/.%2e/.%2e/.%2e/bin/sh",
            "threat_type": "CGI Access",
            "severity": "High"
        },
        {
            "ip": "143.244.150.76",
            "request": "/cgi-bin/%%32%65%%32%65/%%32%65%%32%65/%%32%65%%32%65/%%32%65%%32%65/%%32%65%%32%65/%%32%65%%32%65/%%32%65%%32%65/bin/sh",
            "threat_type": "Shell Access",
            "severity": "High"
        },
        {
            "ip": "143.244.150.76",
            "request": "/cgi-bin/%%32%65%%32%65/%%32%65%%32%65/%%32%65%%32%65/%%32%65%%32%65/%%32%65%%32%65/%%32%65%%32%65/%%32%65%%32%65/bin/sh",
            "threat_type": "CGI Access",
            "severity": "High"
        }
    ]
}
➜  nginxparser git:(main) ✗ 
```