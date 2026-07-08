"""Write a program which contains filter(), map() and reduce()
in it. Python application which contains one list of numbers.
List contains the numbers which are accepted from user. 
Filter should filter out all such numbers which greater 
than or equal to 70 and less than or equal to 90. Map function
will increase each number by 10. Reduce will return product of all that numbers.
"""
from functools import reduce

FilterList=lambda No: No>=70 and No<=90
Increase=lambda No: No+10
Product=lambda No1,No2:No1*No2 

def main():
    n=int(input("Enter number of element:"))

    Data=[]
    print("Enter The Element:")
    for i in range(n):
        Data.append(int(input()))

    print("Input List=",Data)

    Fdata=list(filter(FilterList,Data))
    print("List After Filter:",Fdata)

    Mdata=list(map(Increase,Fdata))    
    print("List After Map:",Mdata)

    Rdata=reduce(Product,Mdata)
    print("Output of Reduce:",Rdata)  

if __name__=="__main__":
    main()      

"""
Input List = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]
List after filter = [76, 89, 86, 90, 70] 
List after map [86, 99, 96, 100, 80]
Output of reduce 6538752000
"""    