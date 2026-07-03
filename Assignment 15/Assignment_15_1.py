""" Write a lambda function using map() which accepts a list of 
numbers and returns a list of squares of each number ."""

Square = lambda no: no*no

def main():
    Data=[1,2,3,4,5,6,7]

    MData=list(map(Square,Data))

    print("Original list:",Data)
    print("Square is :",MData)

if __name__=="__main__":
    main()  

