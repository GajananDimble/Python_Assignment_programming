"""

2.Write a program which Accept one number and prints sum of first N natural Number
"""
def SumNnumber(no):
    sum=0
    for i in range(1,no+1):
        sum+=i
    return sum    

def main():
    no=int(input("Enter a number:"))

    Ret=SumNnumber(no)

    print(Ret)
    
if __name__=="__main__":
    main()  

# Input:5
# Output:15
      