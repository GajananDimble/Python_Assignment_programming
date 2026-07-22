""" Count Lines in a file
Problem Statement: Write A program which accepts a file name from the user and
counts how many lines are present in the file
"""
def CountLines(FileName):
    file=open(FileName,"r")
    count=0

    for line in file:
        count=count+1

    file.close()
    return count

def main():
    Name=input("Enter File Name:")
    Totalines=CountLines(Name)

    print(f"Total Number Of lines in Demo.txt is :{Totalines}")

if __name__=="__main__":
    main()

# Input: Demo.txt
# Expected Output: Total Number of lines in Demo.txt    