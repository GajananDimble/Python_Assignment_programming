"""Write a program which accept name from 
user and display length of its name
"""
def NameLength(name):

    return len(name)

def main():
    Name=input("Accept the name:")

    Ret=NameLength(Name)

    print("Length of name is:",Ret)

if __name__=="__main__":
    main()    