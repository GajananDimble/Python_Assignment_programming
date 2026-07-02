"""

1.Write a program which Accept one number and prints multiplication table of that number
"""
def table(number):
    for i in range (1,11):
        print(number*i,end=" ")

def main():
    Value=int(input("Enter a Number:"))
    Ret=table(Value)

if __name__=="__main__":
    main()

# Input: 4
# OutPut: 4 8 12 16 20 24 28 32 36 40