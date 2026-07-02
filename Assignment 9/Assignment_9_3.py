"""
3. Write a program which accepts one number and prints square of that number.
"""

def Square(no):
    return no*no

def main():
    number=int(input("Enter a number:"))
    ans=Square(number)
    print("Square is :",ans)

if __name__=="__main__":
    main()  

# input:5
# output:25