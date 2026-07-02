"""
Write a Program which accept one number and prints that many numbers starting from 1

"""
def Number(No):
    for i in range(1, No+1):
        print(i,end=" ")

def main():
    num = int(input("Enter a number: "))

    Number(num)
    
if __name__ == "__main__":
    main()    
# input: 5
# output: 1 2 3 4 5