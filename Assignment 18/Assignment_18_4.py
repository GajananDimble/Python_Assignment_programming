""" 4.Write a program which accept N numbers from user and store it into List. Accept one another
number from user and return frequency of that number from List.
"""
def count_frequency(numbers, target):
    return numbers.count(target)

def main():
    Value = int(input("Enter the number of elements : "))
    
    no_list = []
    
    print(f"Enter {Value} numbers:")
    for i in range(Value):
        num = int(input(f"Element {i+1}: "))
        no_list.append(num)
        
    target_num = int(input("\nEnter the number you want to find the frequency of: "))
    
    frequency = count_frequency(no_list, target_num)
    
    print(f"Your List: {no_list}")
    print(f"The number {target_num} appears {frequency} time(s) in the list.")

if __name__ == "__main__":
    main()

"""
Input : Number of elements : 11
Input Elements : 13 5 45 7 4 56 5 34 2 5 65
Element to search : 5
Output : 3
"""