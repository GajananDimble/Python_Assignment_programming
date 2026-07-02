"""
Write a Program which accept two number and print addition,substraction,multiplication
division

"""

def ArithmeticOperations(No1,No2):

    print("Addition is:",       No1+No2)
    print("Substraction is:",   No1-No2)
    print("Multiplication is:", No1*No2)
    print("Division is:",       No1/No2)


def main():
    Number1=int(input("Enter First Number:"))
    Number2=int(input("Enter Second Number:"))
    

    ArithmeticOperations(Number1,Number2)

if __name__=="__main__":
    main()