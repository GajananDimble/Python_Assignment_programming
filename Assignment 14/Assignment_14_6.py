""" Write a lambda function which accept one number and 
returns True if number is odd otherwise false."""

OddNumber=lambda no : no % 2 == 1

def main():
    Value=int(input("Enter Number:"))

    Ans=OddNumber(Value)
    print(Ans)

if __name__=="__main__":
    main()    