"""Create on module named as Arithmetic which contains 4 functions as Add() 
for addition, Sub() for subtraction, Mult() for multiplication and Div()
 for division. All functions accepts two parameters as number and perform 
 the operation. Write on python program which call all the functions from 
 Arithmetic module by accepting the parameters from user
"""
import Arithmetic

def main():
    a=int(input("Enter First Number:"))
    b=int(input("Enter Second Number:"))  

    print("Addition is:",Arithmetic.Add(a,b))  
    print("Substration is:",Arithmetic.Sub(a,b))  
    print("Multiplication is:",Arithmetic.Mult(a,b))  
    print("Division is:",Arithmetic.Div(a,b)) 
    
if __name__=="__main__":
    main()    