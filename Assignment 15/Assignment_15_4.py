""" Write a lambda function using reduce() which accepts a list of 
numbers and returns the Addition of all elements ."""

from functools import reduce

AdditionList = lambda No1,No2: No1+No2

def main():
    Data=[11,21,31,51]

    RData=reduce(AdditionList,Data)

    print("Original Data:",Data)
    print("Addition is:",RData)            #114

if __name__=="__main__":
    main()  
