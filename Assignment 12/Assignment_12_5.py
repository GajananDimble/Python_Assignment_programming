"""
Write a Program which accept one number and prints that many number in reverse order

"""
def Reverse(No):
    for i in range(No,0,-1):
        print(i,end=" ")

def main():
    num = int(input("Enter a number: "))

    Reverse(num)
    
if __name__ == "__main__":
    main() 

# input: 5
# output: 5 4 3 2 1    