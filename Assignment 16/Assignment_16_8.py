""" Write a program which accept number from user and print
that number of "*" on screen.
"""
def Display(No):
    for i in range(No):
        print("*",end=" ")

def main():
    value=int(input("Enter The Number"))

    Display(value)

if __name__=="__main__":
    main()    