""" Write a lambda function which accept one number and 
returns Cube of that number."""


Cube = lambda no: no*no*no

def main():
    number=int(input("Enter a number:"))

    ans=Cube(number)
    print("Cube is :",ans)

if __name__=="__main__":
    main()  

# input:5
# output:25