""" Copy File Contents into Another File
Problem Statement:
     Write A program which accepts two file names from the user
     . First file is an existing file
     . Second File is a new file

     copy all contents from the first file into second file.
"""

def CopyFile(FirstFile,SecondFile):
    File1=open(FirstFile,"r")
    File2=open(SecondFile,"w")

    for Data in File1:
        File2.write(Data)

    File1.close()
    File2.close()

def main():
    FileName1=input("Enter First File Name:")
    FileName2=input("Enter Second File Name:")

    CopyFile(FileName1,FileName2)

    print(f"Contents of {FileName1} Copied into {FileName2}")

if __name__=="__main__":
    main()

# Input: ABC.txt Demo.txt
# Expected Output: Contents of ABC.txt copied into Demo .text  