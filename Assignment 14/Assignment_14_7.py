""" Write a lambda function which accept one number and 
returns True if divisible by 5."""

TrueValue=lambda no : no % 5 == 0

def main():
    Value=int(input("Enter Number:"))

    Ret=TrueValue(Value)
    print(Ret)

if __name__=="__main__":
    main()    