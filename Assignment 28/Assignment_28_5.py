""" Search a Word in  file
Problem Statement: Write A program which accepts a file name from the user and
Checks whether that word is present in the file or not
"""

def SearchWord(FileName,word):
    File=open(FileName,"r")
    data=File.read()

    if word in data:
        print(f"Display whether the {word} is found in Demo.txt")
    else:
        print(f"Display whether the {word} is not found in Demo.txt")

    File.close()

def main():
    Name=input("Enter File Name:")
    Word=input("Enter Word to search:")

    SearchWord(Name,Word)

if __name__=="__main__":
    main()

# Input: Demo.txt Marvellous
# Expected Output: Display whether the word Marvellous is found in Demo.txt or not  