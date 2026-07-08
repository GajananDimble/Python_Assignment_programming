""" 5.Write a program which accept N numbers from user and store it into List. Return addition of all
prime numbers from that List. Main python file accepts N numbers from user and pass each
number to ChkPrime() function which is part of our user defined module named as
MarvellousNum. Name of the function from main python file should be ListPrime().
"""

import MarvellousNum

def ListPrime(number):
    total_prime_sum=0

    for num in number:
        if MarvellousNum.ChkPrime(num):
            total_prime_sum +=num

    return total_prime_sum        

def main():
    Value = int(input("Number of Elements :"))

    no_list=[]

    print(f"Enter {Value} numbers (integers preferred for prime checking):")
    for i in range(Value):
        num = int(input(f"Element {i+1}: "))
        no_list.append(num)

    prime_sum = ListPrime(no_list)

    print(f"Your List: {no_list}")
    print(f"Sum of all prime numbers: {prime_sum}")
       

if __name__ == "__main__":
    main()

"""
Input : Number of elements : 11
Input Elements : 13 5 45 7 4 56 10 34 2 5 8
Output : 32 (13 + 5 + 7 +2 + 5)
"""