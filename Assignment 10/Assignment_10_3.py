"""

3.Write a program which Accept one number and prints factorial pf that number
"""
def Factorial(no):
    fact=1

    for i in range(1,no+1):
            fact*=i
    return fact

def main():
    no=int(input("Enter a number:"))

    Ret=Factorial(no)
    print(Ret)

if __name__=="__main__":
    main() 

# Input:5
# Output:120