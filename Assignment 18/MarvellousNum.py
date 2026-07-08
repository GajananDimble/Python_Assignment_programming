""" 5.Write a program which accept N numbers from user and store it into List. Return addition of all
prime numbers from that List. Main python file accepts N numbers from user and pass each
number to ChkPrime() function which is part of our user defined module named as
MarvellousNum. Name of the function from main python file should be ListPrime().
"""
# MarvellousNum.py -> Module

def ChkPrime(num):
    if num <= 1:
        return False
    
    n=int(num)
    for i in range(2,n):
        if  n % i == 0:
            return False 
        
    return True 

"""
Input : Number of elements : 11
Input Elements : 13 5 45 7 4 56 10 34 2 5 8
Output : 32 (13 + 5 + 7 +2 + 5)
"""