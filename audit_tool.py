#!/usr/bin/env python3
"""
writing the whole program myself
"""
import sys


if len(sys.argv)<2 :
    print("You did not provide the file name.")
    print("Run the script this way:./script_name file_name")
    sys.exit(1)

logfile=sys.argv[1]

count=0
try :
    with open(logfile,"r") as f:
        for line in f:
            if "INFO" in line or "WARNING" in line or "ERROR" in line:
                count+=1

        print("seccessfully reading the file.")
except FileNotFoundError :
    print("Could not find the file.")
    sys.exit(1)
except Exception as e:
    print("something went wrong.")

with open ("audit_summary.txt","w")as f:
    f.write(f"Total log matches: {count}\n")
    f.write("we seccessfully complete the project")