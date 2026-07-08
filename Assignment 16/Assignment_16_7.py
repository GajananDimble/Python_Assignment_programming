"""Writ a program which contain one function that accepts one number from 
 user and returns true if number is divisible by 5 otherwise return false
"""
def CheckDiv(No):
    if No % 5==0:
        return True
    else:
        return False

def main():
    Value=int(input("Enter number:"))

    Ret=CheckDiv(Value)

    print(Ret)

if __name__=="__main__":
    main()
# Input:8         Output: False
# Input:25        Output: True