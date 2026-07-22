""" Frequency of a string in file
Problem Statement:
     Write A program which accepts a file name and one string from the user and 
     returns the frequency(count of occurrences) of that string in the file
"""
import sys

def CountFreq(FileName,word):
    file=open(FileName,"r")

    Data=file.read()
    words=Data.split()

    count=0
    for value in words:
        if value==word:
            count=count+1

    file.close()
    return count
    
def main():
    Name=input("Enter File Name:")
    Word=input("Enter word:")

    Ret=CountFreq(Name,Word)

    print(f"Frequency of {Word} is :{Ret}")
if __name__=="__main__":
    main()

# Input: Demo.txt Marvellous
# Expected Output: Count how many times "Marvellous" appears in Demo.txt