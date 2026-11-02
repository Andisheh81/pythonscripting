#!/usr/bin/env python3
"""
Title: Safe Log Reader
Description: Demonstrates robust error handling using try/except blocks.
"""

import sys

TARGET_FILE = "non_existent_system.log"

def read_secure_log():
    print(f"Attempting to read secure log: {TARGET_FILE}...")
    
    try:
        # Try to open a file that hasn't been created
        with open(TARGET_FILE, "r") as f:
            data = f.read()
            print("File contents loaded successfully.")
            
    except FileNotFoundError:
        print(f"DEFENSE TRIGGERED: The file '{TARGET_FILE}' was not found.")
        print("Action: Creating a default log placeholder automatically...")
        
        # Recover by creating the file on the fly
        with open(TARGET_FILE, "w") as f:
            f.write("INFO: Default log created due to missing file.\n")
        print("Recovery complete! Default file initialized.")
        
    except Exception as e:
        # Catch any other unexpected system errors
        print(f"CRITICAL ERROR: An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    read_secure_log()