"""Write a program which contains one function named as CheckNum() which accept one
parameter as number.If number is even then it should display "Even number"otherwise
display "odd number" on console."""

def CheckNum(No):
    if No %2==0:
        print("Even Number")
    else:
        print("Odd Number")    

def main():
    Value=int(input("Enter number:"))

    CheckNum(Value)

if __name__=="__main__":
    main()    

# Input:11       Output:Odd Number
# Input:8        OutPut:Even Number    