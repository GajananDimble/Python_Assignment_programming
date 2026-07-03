""" Write a lambda function using filter() which accepts a list of 
numbers and returns a list of odd number ."""

OddNumber = lambda no: no%2==1

def main():
    Data=[1,2,3,4,5,6,7,8,11]

    fData=list(filter(OddNumber,Data))

    print("Original list:",Data)
    print("Odd Numbers :",fData)

if __name__=="__main__":
    main()  