""" 3.Write a program which accept N numbers from user and store it into List. Return Minimum
number from that List.
"""
def Minimum_Number(No):
    return min(No)

def main():
    Value = int(input("Number of Elements :"))

    no_list=[]

    print(f"Enter {Value} number:")
    for i in range(Value):
        num = int(input(f"Element {i+1}: "))
        no_list.append(num)

    min_num = Minimum_Number(no_list)     

    print(f"Your List: {no_list}")
    print(f"Minimum number is: {min_num}")       

if __name__ == "__main__":
    main()

"""
Input : Number of elements : 4
Input Elements : 13 5 45 7
Output : 5
"""