"""

5.Write a program to Accept one number and check whether it is divisible by 3 and 5
"""

def CheckDivisible(no):
    if no % 3 == 0 and no % 5 == 0:
        print("Divisible by 3 and 5")
    else:
        print("Not Divisible by 3 and 5")

def main():
    number=int(input("Enter a Number:"))
    CheckDivisible(number)      

if __name__=="__main__":
    main()