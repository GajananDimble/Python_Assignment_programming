"""write a program that calculates factorials of multiple numbers
simultaneously using pool.map() display procees id,input number,factorial
"""
from multiprocessing import Pool
import os
import time

def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i

    print("Process ID:",os.getpid(),
          "Input :",n,
          "Factorial:",fact)    

def main():
    start_time=time.perf_counter()
    Value =int(input("Enter  Number Of elements:"))

    Data=[]
    print("Enter The Element:")
    for i in range(Value):
        Data.append(int(input()))
    
    p=Pool()
    results = p.map(factorial,Data)

    p.close()
    p.join()
        
    end_time=time.perf_counter()
    

    print(f"time requred:{end_time-start_time:.4f}")    

if __name__=="__main__":
    main()

"""
Input
[10,15,20,25]
Display
• Process ID
• Input Number
• Factorial
"""