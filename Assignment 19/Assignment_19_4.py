"""Write a program which contains filter(), map() and reduce() in it
Python application which contains one list of numbers. 
List contains the numbers which are accepted from user.
Filter should filter out all such numbers which are even.
Map function will calculate its square. Reduce will return addition of all that numbers.
"""

from functools import reduce

FilterList=lambda No: No % 2 == 0
Cal_Square=lambda No: No**2
Product=lambda No1,No2:No1+No2

def main():
    n=int(input("Enter number of element:"))

    Data=[]
    print("Enter The Element:")
    for i in range(n):
        Data.append(int(input()))

    print("Input List=",Data)

    Fdata=list(filter(FilterList,Data))
    print("List After Filter:",Fdata)

    Mdata=list(map(Cal_Square,Fdata))    
    print("List After Map:",Mdata)

    Rdata=reduce(Product,Mdata)
    print("Output of Reduce:",Rdata)  

if __name__=="__main__":
    main()      

"""
Input List = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10] 
List after filter = [2, 4, 4, 2, 8, 10]
List after map [4, 16, 16, 4, 64, 100]
Output of reduce = 204
"""    