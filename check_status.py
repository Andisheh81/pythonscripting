#!/usr/bin/env python3
import subprocess
import sys

# Let's run a command that we know exists ('ls')
command = ["ls", "-l"]

print(f"Executing command: {' '.join(command)}")
result = subprocess.run(command, capture_output=True, text=True)

# Check the return code
if result.returncode == 0:
    print("SUCCESS: The command executed without issues.")
    print("Output:")
    print(result.stdout)
else:
    print(f"ERROR: The command failed with exit code {result.returncode}")
    print("Error details:")
    print(result.stderr)
    sys.exit(1)