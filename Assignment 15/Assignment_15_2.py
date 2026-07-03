""" Write a lambda function using filter() which accepts a list of 
numbers and returns a list of even  number ."""

EvenNumber = lambda no: no%2==0

def main():
    Data=[1,2,3,4,5,6,7,8,10,14,18,20]

    fData=list(filter(EvenNumber,Data))

    print("Original list:",Data)
    print("Even Numbers :",fData)

if __name__=="__main__":
    main()  
