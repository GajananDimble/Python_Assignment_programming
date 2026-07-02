"""
Write a Program which accept one number and prints count of digits in that number

"""
def Count(No):
    No = abs(No)

    if No  == 0:
        return 1
    
    count = 0
    while No > 0:
        count +=1
        No //= 10
    return count

def main():
    Value = int(input("Enter Number :"))
    Ret = Count(Value)
    print(Ret)

if __name__ == "__main__":
    main()

# Input: 7521
# Output: 4