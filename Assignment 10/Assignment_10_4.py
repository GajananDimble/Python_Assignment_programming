"""

4.Write a program which Accept one number and prints all even number till that number
"""
def Even(No):
     for i in range(2,No+1,2):
        print(i,end=" ") 

def main():
    no=int(input("Enter a number:"))

    Ret=Even(no)

if __name__=="__main__":
    main()  

# Input:10
# Output:2 4 6 8 10