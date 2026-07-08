""" 1.Write a program which accept N numbers from user and store it into List. Return addition of all
elements from that List.
"""
def Addition(numbers):
    return sum(numbers)

def main():
    n = int(input("Enter the number of elements: "))
    
    no_list = []
    
    print("Enter numbers:",n)
    for i in range(n):
        num = int(input(f"Element{i+1} :"))
        
        no_list.append(num)
        
    total_sum = Addition(no_list)
    
    print(f"Your List: {no_list}")
    print(f"Sum of all elements: {total_sum}")

if __name__ == "__main__":
    main()

"""
Input : Number of elements : 6
Input Elements : 13 5 45 7 4 56
Output : 130
"""