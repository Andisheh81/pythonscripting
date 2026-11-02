#!/usr/bin/env python3
"""
Title: System Log Analyzer
Description: Writes mock system logs and parses them for errors.
"""

import os

LOG_FILE = "system_diagnostic.log"

def generate_mock_logs():
    """Creates a sample log file with mixed status messages."""
    print(f"Generating mock log file: {LOG_FILE}...")
    log_data = [
        "INFO: System boot completed successfully.",
        "INFO: Network interface eth0 active.",
        "WARNING: High memory usage detected (85%).",
        "INFO: User login successful: admin.",
        "ERROR: Failed to connect to database server on port 5432.",
        "INFO: Backup routine completed."
    ]
    
    # 'w' mode opens the file for writing
    with open(LOG_FILE, "w") as f:
        for line in log_data:
            f.write(line + "\n")
    print("Mock logs written successfully.\n")

def parse_errors():
    """Reads the log file line by line and filters for 'ERROR'."""
    print(f"Scanning {LOG_FILE} for critical errors...")
    print("-" * 50)
    
    error_count = 0
    
    # 'r' mode opens the file for reading (this is the default)
    with open(LOG_FILE, "r") as f:
        for line_num, line in enumerate(f, 1):
            # .strip() removes trailing newline characters
            clean_line = line.strip()
            
            if "ERROR" in clean_line:
                error_count += 1
                print(f"[Line {line_num}] CRITICAL: {clean_line}")
            elif "WARNING" in clean_line:
                print(f"[Line {line_num}] ALERT:    {clean_line}")

    print("-" * 50)
    print(f"Scan complete. Found {error_count} error(s).")

if __name__ == "__main__":
    generate_mock_logs()
    parse_errors()