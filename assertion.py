import re

log_entries = [
    "Error status: ERR-404 severity: DEBUG",
    "Error status: ERR-500 severity: CRITICAL",
    "Error status: ERR-503 severity: CRITICAL",
    "Error status: ERR-403 severity: WARNING"
]

# Pattern: Match "ERR-" and digits, BUT ONLY IF followed by " severity: CRITICAL"
# Notice that "(?=\s+severity:\s+CRITICAL)" does not consume characters—it just checks ahead.
pattern = r"ERR-\d+(?=\s+severity:\s+CRITICAL)"

for line in log_entries:
    match = re.search(pattern, line)
    if match:
        print(f"Matched critical error code: {match.group()}")

# Output:
# Matched critical error code: ERR-500
# Matched critical error code: ERR-503
print("*" *20)

log_line = "Transaction log: target_id 9912, user: root_admin, action: login"

# Positive Lookbehind: Look behind for "user: " before matching the alphanumeric username (\w+)
pattern1 = r"(?<=user: )\w+"

match1 = re.search(pattern1, log_line)

if match1:
    print(f"Extracted username: {match1.group()}")
    
# Output: Extracted username: root_admin