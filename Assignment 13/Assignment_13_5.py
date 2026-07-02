"""
Write a Program which accept marks and display grade

"""
def Grade(Marks):
    if Marks>=75:
        print("Your Grade is Distinction")
    elif Marks>= 60:
        print("Your Grade is First Class")
    elif Marks>=50:
        print("Your Grade is Second Class") 
    else:
        print("Your Are Fail")       

def main():
    No=int(input("Enter The Grade:"))

    Grade(No)

if __name__=="__main__":
    main()    