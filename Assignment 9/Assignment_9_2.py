"""
2. Write a program which contains one function ChkGreater() that accept two numbers
and print the greater number
"""

def CheckGreater(No1,No2):
    if No1>No2:
        print(No1,"is greater")
    else:
        print(No2,"is greater")  

def main():
    Value1=int(input("Enter First Number:")) 
    Value2=int(input("Enter Second Number:"))          

    CheckGreater(Value1,Value2)  

if __name__=="__main__":
    main()    

# input:10 20
# output:20 is greater