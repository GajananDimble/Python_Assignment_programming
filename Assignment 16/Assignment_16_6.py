""" Write a program which accept number from user and check whether that 
number is positive or negative or zero
"""

def CheckNum(No):
    if No>0:
        print("Positive Number")
    elif No<0:
        print("Negative Number")    
    else:
        print("Zero")    

def main():
    Value=int(input("Enter number:"))

    CheckNum(Value)

if __name__=="__main__":
    main()    

# Input:11       Output:Positive Number
# Input:-8       OutPut:Negative Number   
# Input:-        OutPut:Zero 