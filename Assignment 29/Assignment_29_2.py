"""Display File Content
Problem Statement: Write A program which accepts a file name from the user and
opens that file,and displays the entire contents on the console
"""

def DispayFile(FileName):
    File=open(FileName,"r")

    Data=File.read()
    print(Data)

    File.close()

def main():
    Name=input("Enter File Name:")
    DispayFile(Name)

if __name__=="__main__":
    main()

# Input: Demo.txt
# Expected Output: Display contents of Demo.txt on console
