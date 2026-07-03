""" Write a lambda function which accept three numbers and 
returns largest number."""

LargestNumber = lambda No1 , No2 ,No3 : max(No1,No2,No3)
    
def main():
    Value1=int(input("Enter First Number:")) 
    Value2=int(input("Enter Second Number:"))
    Value3=int(input("Enter Third Number:"))

    Ret=LargestNumber(Value1,Value2,Value3)

    print("Largest Number is: ",Ret)

if __name__=="__main__":
    main()    

# input:10 20 16
# output:20