"""for every number in the given list count how many prime 
numbers exist between 1 and n using multiprocessing pool"""

from multiprocessing import Pool
import time

def count_primes(n):
    count=0
    for i in range(2,n+1):
        prime=True

        for j in range(2,i):
            if i%j==0:
                prime=False
                break
        if prime:
            count+=1    
    return count
def main():
    start_time=time.perf_counter()
    Value =int(input("Enter  Number Of elements:"))

    Data=[]
    print("Enter The Element:")
    for i in range(Value):
        Data.append(int(input()))

    p=Pool()
    results = p.map(count_primes,Data)

    p.close()
    p.join()
    
    end_time=time.perf_counter()


    print("Input is:",Data)
    print("Prime Counts:",results)
    print(f"Time Required:{end_time-start_time:.3f}")

if __name__ == "__main__":
    main()
    
# Input is: [10000, 20000, 30000, 40000]
# Prime Counts: [1229, 2262, 3245, 4203]
# Time Required:20.629

