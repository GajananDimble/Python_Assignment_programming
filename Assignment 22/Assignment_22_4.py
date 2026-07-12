""" Wrirte thr program that calculates
1^5+2^5+3^5+.....+N^5
for multiple values of N simultaneously using Pool.
"""

from multiprocessing import Pool
import os
import time

def calculate_sum(n):
    total=0

    for i in range(1,n+1):
        total=total+(i**5)

    print("Process ID:",os.getpid(),
        "Input :",n,
        "Sum:",total)   

def main():
    start_time=time.perf_counter()
    Value =int(input("Enter  Number Of elements:"))

    Data=[]
    print("Enter The Element:")
    for i in range(Value):
        Data.append(int(input()))

    p=Pool()

    p.map(calculate_sum,Data)

    p.close()
    p.join()
    
    end_time=time.perf_counter()
    print(f"Input time Required:{end_time-start_time:.3f}")

if __name__ == "__main__":
    main()

    
"""
Input
[1000000,
2000000,
3000000,
4000000]
Measure total execution time.
"""