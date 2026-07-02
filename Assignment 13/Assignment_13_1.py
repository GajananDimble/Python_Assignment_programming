"""
Write a Program which accept length and width of rectangle and prints area

"""
def AreaOfRectangle(Length,Width):
    Area=Length*Width
    print("Area of Rectangle:",Area)

def main():
    number1=float(input("Enter Length:"))
    number2=float(input("Enter Width:"))

    Ret=AreaOfRectangle(number1,number2)

if __name__=="__main__":
    main()       