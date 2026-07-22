"""Check File Exists in Current Directory
Problem Statement: Write A program which accepts a file name from the user and
checks whether that file exists in the current Directory or not
"""
import os

def CheckFile(FileName):
    if os.path.exists(FileName):
        print(f"{FileName} is exists in Current Directory")
    else:
        print(f"{FileName} is Does Not exists in Current Directory:")

def main():
    Name=input("Enter File Name:")
    
    CheckFile(Name)

if __name__=="__main__":
    main()

# Input: Demo.txt
# Expected Output: Display whether Demo.txt exists or Not
