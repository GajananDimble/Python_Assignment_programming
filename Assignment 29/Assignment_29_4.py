""" Compare Two Files(Command Line)
Problem Statement:
     Write A program which accepts two file names through command 
     line arguments and compares the contents of both files
     . If both files contain the same contents,display success
     . Otherwise display Failure
"""
import sys

def CompareFile(FileName1,FileName2):
    fobj1=open(FileName1,"r")
    fobj2=open(FileName2,"r")


    Data1=fobj1.read()
    Data2=fobj2.read()

    fobj1.close()
    fobj2.close()

    if Data1==Data2:
        print("Success")
    else:
        print("Failue")    

    
def main():
    CompareFile(sys.argv[1],sys.argv[2])

if __name__=="__main__":
    main()

# Input: Demo.txt Hello.txt
# Expected Output: Success OR Failure 