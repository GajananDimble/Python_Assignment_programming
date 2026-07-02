"""
Write a Program which accept radius of circle and prints area of circle

"""
def RadiusCircle(Radius):
    PI=3.14
    Radius=PI*(Radius*Radius)
    print("Area of Circle:",Radius)

def main():
    Value=float(input("Enter Radius:"))

    Ret=RadiusCircle(Value)

if __name__=="__main__":
    main()    