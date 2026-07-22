""" Display File line by line
Problem Statement: Write A program which accepts a file name from the user and
Displays the contents of the file line by line on the screen
"""
def DisplayLine(FileName):
    file=open(FileName,"r")

    for line in file:
        print(line, end="")

    file.close()  
     
def main():
    Name=input("Enter File Name:")
    DisplayLine(Name)

if __name__=="__main__":
    main()

# Input: Demo.txt
# Expected Output: Display each line of Demo.txt one by one    