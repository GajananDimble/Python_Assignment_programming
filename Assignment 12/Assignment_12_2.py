"""
Write a Program which accept one number and prints its factor

"""
def factors(no):
    print("Factoes are:")
    for i in range(1, no+1):
        if no % i == 0:
            print(i,end=" ")

def main():
    num = int(input("Enter a number: "))
    factors(num)

if __name__ == "__main__":
    main()