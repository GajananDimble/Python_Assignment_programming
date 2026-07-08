"""Write a program which contains one function named as Add() which accept two 
numbers from user and return addition of that two numbers.
"""

def Add(No1,No2):
    return No1+No2

def main():
    Number1=int(input("Enter First Number:"))
    Number2=int(input("Enter Second Number:"))  

    Ret=Add(Number1,Number2)

    print("Addition is:",Ret)  

if __name__=="__main__":
    main()  

# input: 11 5    Output:16      