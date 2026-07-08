"""Write a program which contains one lambda function which
accepts two parameters and returns their multiplication."""

Multiply=lambda No1,No2: No1*No2

def main():
    Value1=int(input("Enter Number:"))
    Value2=int(input("Enter Number:"))

    print("Output:",Multiply(Value1,Value2))

if __name__=="__main__":
    main()
