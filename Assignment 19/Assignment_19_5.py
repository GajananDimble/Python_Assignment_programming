"""Write program which contains filter(), map() and reduce() in it
Python application which contains one list of numbers. 
List contains the numbers which are accepted from user. 
Filter should filter out all prime numbers. Map function will
multiply each number by 2. Reduce will return Maximum number
from that numbers. (You can also use normal functions instead of lambda functions).
"""

from functools import reduce
def Checkprime(No):
    if No <= 1:
        return False
    
    for i in range(2, int(No ** 0.5) + 1):
        if No % i == 0:
            return False
        
    return True

FilterPrime=lambda No: Checkprime(No)
Multiply=lambda No: No*2

def Maximum(No1,No2):
    if No1>No2:
        return No1
    else:
        return No2
def main():
    n=int(input("Enter number of element:"))

    Data=[]
    print("Enter The Element:")
    for i in range(n):
        Data.append(int(input()))

    print("Input List=",Data)

    Fdata=list(filter(FilterPrime,Data))
    print("List After Filter:",Fdata)

    Mdata=list(map(Multiply,Fdata))    
    print("List After Map:",Mdata)

    Rdata=reduce(Maximum,Mdata)
    print("Output of Reduce:",Rdata)  

if __name__=="__main__":
    main()      

"""
Input List = [2, 70, 11, 10, 17, 23, 31, 77] 
List after filter [2, 11, 17, 23, 31] 
List after map [4, 22, 34, 46, 62]8
Output of reduce = 62
"""    