""" Count Words in a file
Problem Statement: Write A program which accepts a file name from the user and
counts the total number of words in that file
"""
def CountWords(FileName):
    file=open(FileName,"r")
    count=0

    for line in file:
        words=line.split()
        count=count+len(words)

    file.close()
    return count

def main():
    Name=input("Enter File Name:")
    TotalWords=CountWords(Name)
    
    print(f"Total Number Of Words in Demo.txt is:{TotalWords}")

if __name__=="__main__":
    main()

# Input: Demo.txt
# Expected Output: Total Number of Words in Demo.txt    