""" Write a lambda function using filter() which accepts a list of 
numbers and returns the maximum elements ."""

from functools import reduce

MaximumElements = lambda No1,No2:No1 if No1 > No2 else No2 

def main():
    Data=[12,15,18,51,101]

    RData=reduce(MaximumElements,Data)

    print("Original Data",Data)
    print("Maximum Element:",RData)

if __name__=="__main__":
    main()  
