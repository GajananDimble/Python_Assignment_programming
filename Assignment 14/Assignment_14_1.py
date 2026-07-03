""" Write a lambda function which accept one number and 
returns square of that number."""

Square = lambda no: no*no

def main():
    number=int(input("Enter a number:"))

    ans=Square(number)
    print("Square is :",ans)

if __name__=="__main__":
    main()  

# input:5
# output:25