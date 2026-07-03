""" Write a lambda function which accept two number and 
returns Multiplication ."""

Multiplication = lambda No1 , No2 : No1 * No2
    
def main():
    Value1=int(input("Enter First Number:")) 
    Value2=int(input("Enter Second Number:"))

    Ans=Multiplication(Value1,Value2)

    print("Multiplication is: ",Ans)

if __name__=="__main__":
    main()    

# input:10 3
# output:30 