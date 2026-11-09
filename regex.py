import re
"""
log_line = "2026-11-09 18:45:12 [WARN] Admin user 'root_admin' failed login from IP 10.0.4.55 - Error Code: ERR-9021."

# 1. Using re.search() so we can use .group()
reg = r"ERR-\d{4}"
match = re.search(reg, log_line)

if match:
    print(f"Here is the result: {match.group()}")
else:
    print("No result found")

# 2. Escaping the dots (\.) and using \d{1,3} for safety across all IP ranges
ip_pattern = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
subst = "[REDACTED]"

# re.sub returns a plain string, so we print it directly
redacted_log = re.sub(ip_pattern, subst, log_line)
print(f"Redacted log line:{redacted_log}")
"""


log_line = "2026-11-09 18:45:12 [WARN] Admin user 'root_admin' failed login from IP 10.0.4.55 - Error Code: ERR-9021."

# Build a pattern with 4 capturing groups ()
# Group 1: Timestamp (YYYY-MM-DD HH:MM:SS)
# Group 2: Log Level (WARN, ERROR, etc.)
# Group 3: Username
# Group 4: IP Address
pattern = r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) \[([A-Z]+)\] Admin user '(\w+)' failed login from IP (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"

match = re.search(pattern, log_line)

if match:
    print("--- Successfully Parsed Log ---")
    print(f"Timestamp : {match.group(1)}")
    print(f"Log Level : {match.group(2)}")
    print(f"Username  : {match.group(3)}")
    print(f"IP Address: {match.group(4)}")
    
    # Or grab them all as a tuple at once:
    print("\nAll groups tuple:", match.groups())
else:
    print("No match found.")