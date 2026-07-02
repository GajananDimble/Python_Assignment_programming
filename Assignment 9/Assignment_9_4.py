"""
4. Write a program which accepts one number and prints Cube of that number.
"""

def Cube(no):
    return no*no*no

def main():
    Value=int(input("Enter a number:"))
    ans=Cube(Value)
    print("Cube is number:",ans)

if __name__=="__main__":
    main()

# input:6
# output:216