""" Write a lambda function using filter() which accepts a list of 
numbers and returns the minimum elements ."""

from functools import reduce

MinimumElements = lambda No1,No2:No1 if No1 < No2 else No2 

def main():
    Data=[12,15,18,51,101]

    RData=reduce(MinimumElements,Data)

    print("Original Data:", Data)
    print("Minimum Element:", RData)

if __name__=="__main__":
    main()  
