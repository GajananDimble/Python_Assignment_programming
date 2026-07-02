"""

4.Write a program which Accept one number and prints all odd number till that number
"""
def odd(No):
     for i in range(1,No+1,2):
        print(i,end=" ") 

def main():
    no=int(input("Enter a number:"))

    Ret=odd(no)

if __name__=="__main__":
    main()

# Input:12
# Output:1 3 5 7 9 11  