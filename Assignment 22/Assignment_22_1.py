"""write a program that accept a list of integers in uses Pool.map() to calculate
the sum of squres from 1 to n for every elemnt in the list"""

from multiprocessing import Pool
import time

def sum_of_squares(n):
    total=0
    for i in range(1,n+1):
        total=total+(i*i)

    return total
    
def main():
    start_time=time.perf_counter()

    Value =int(input("Enter  Number Of elements:"))

    Data=[]
    print("Enter The Element:")
    for i in range(Value):
        Data.append(int(input()))
    
    print(f"Original list: {Data}")

    p=Pool()

    result=p.map(sum_of_squares,Data)
    p.close()
    p.join()

    print("Sum of squres:",result)
    
    end_time=time.perf_counter()    

    print(f"Time is require:{end_time-start_time:.4f}")

if __name__ == "__main__":
    main()

    """
Example Input
[1000000,2000000,3000000,4000000]
Expected Output
[333333833333500000,
2666668666667000000,
...
]
"""