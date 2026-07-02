"""
Write a Program which accept one number and check whether it is palindrome or not

"""
def Palindrome(No):
    if No < 0:
        return "Not Palindrome"
    
    SequenceNum = No
    
    ReverseNum = 0
    while No > 0:
        Ans = No % 10
        ReverseNum = (ReverseNum * 10) + Ans
        No = No // 10

    if SequenceNum == ReverseNum:
        return "Palindrome"
    else:
        return "Not Palindrome"
    
def main():
    Value = int (input("Enter Number :"))
    Ret  = Palindrome(Value)  
    print(Ret)

if __name__ == "__main__":
    main()

# Input: 121
# Output: Palindrome