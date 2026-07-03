""" Write a lambda function which accept two number and 
returns minimum of number."""

CheckMinimum =lambda No1 ,No2: No1 if No1 < No2 else No2
    
def main():
    Value1=int(input("Enter First Number:")) 
    Value2=int(input("Enter Second Number:"))

    Ret=CheckMinimum(Value1,Value2)

    print("The Minimum Number is :",Ret)


if __name__=="__main__":
    main()    

# input:10 20
# output:10 is minimum