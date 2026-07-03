""" Write a lambda function which accept one number and 
returns True if number is even otherwise false."""

EvenNumber=lambda no : no % 2 == 0

def main():
    Value=int(input("Enter Number:"))

    Ans=EvenNumber(Value)
    print(Ans)

if __name__=="__main__":
    main()    