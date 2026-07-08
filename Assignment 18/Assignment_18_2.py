""" 2.Write a program which accept N numbers from user and store it into List. Return Maximum
number from that List.
""" 

def Maximum_Number(No):
    return max(No)

def main():
    Value = int(input("Number of Elements :"))

    no_list=[]

    print(f"Enter {Value} number:")
    for i in range(Value):
        num = int(input(f"Element {i+1}: "))
        no_list.append(num)

    max_num = Maximum_Number(no_list)     

    print(f"Your List: {no_list}")
    print(f"Maximum number is: {max_num}")       

if __name__ == "__main__":
    main()
    
"""
Input : Number of elements : 7
Input Elements : 13 5 45 7 4 56 34
Output : 56
"""