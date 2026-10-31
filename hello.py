import sys
import os

# 1. Check if the user forgot to provide any arguments at all
if len(sys.argv) < 2:
    print("ERROR: Please provide at least one folder name!")
    print("Usage: python3 tool.py [folder1] [folder2] [folder3] ...")
    sys.exit(1)

# 2. Loop through every argument starting from index 1 onward
for folder_name in sys.argv[1:]:
    print("-" * 40)
    
    # 3. Apply our safety and creation logic to each item
    if os.path.exists(folder_name):
       
        os.rmdir(folder_name)
        print(f"deleting the file'{folder_name}'")

print("-" * 40)
print("All tasks completed successfully!")