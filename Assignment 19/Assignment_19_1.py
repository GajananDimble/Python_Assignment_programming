"""Write a program which contains one lambda function which 
 accepts one parameter and returns the power of two
"""

power=lambda x:x**2

def main():
    Value=int(input("Enter Number:"))

    print("Output:",power(Value))

if __name__=="__main__":
    main()
