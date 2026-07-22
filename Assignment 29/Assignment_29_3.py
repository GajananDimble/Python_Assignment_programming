"""Copy File Contents into a New File (Command Line)
Problem Statement:
    Write a program which accepts an existing file name through
command line arguments, creates a new file named Demo.txt,
and copies all contents from the given file into Demo.txt.
"""
import sys

def CopyFile(FileName):
    File1=open(FileName,"r")
    File2=open("Demo.txt","w")

    for line in File1:
        File2.write(line)

    File1.close()
    File2.close()

    print(f"Create Demo.txt and copy contents of {FileName} into Demo.txt ")

def main():
    CopyFile(sys.argv[1])

if __name__=="__main__":
    main()

# Input: ABC.txt 
# Expected Output: Create Demo.txt and copy contents of ABC.txt into Demo.txt  