#Answers to the coding exercises in this URL - 
#https://www.codingninjas.com/studio/library/30-most-common-accenture-coding-questions


"""
10. Execute the function for the given purpose.
Create a matrix and mention the elements in it. 
Now, divide the main matrix into two halves in such a way that the elements 
in index 0 are even, the elements in index 1 are odd, and so on.

Then arrange the values in ascending order for even and odd. 
After this, calculate the sum of the second largest numbers from both even and odd matrices.

Example
The size of the array is 5.
Element at 0 index: 3
Element at 1 index: 4
Element at 2 index: 1
Element at 3 index: 7
Element at 4 index: 9

Even array: 1,3,9
Odd array: 4,7
"""

def sort_arr(arr, desc=False):
    # Here i have used sorting algo
    for i in range(0, len(arr)-1):
        for j in range(1, len(arr)):
            if arr[i] > arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp

    return arr

def largeSmallSum(arr):
    # First create separate array of odd and even positioned elements.

    odd_arr = []
    even_arr = []
    for i in range(0, len(arr)):
        if (i % 2) == 0:
            even_arr.append(arr[i])
        else:
            odd_arr.append(arr[i])

    # Sort the arrays in ascending order
    sorted_even_arr = sort_arr(even_arr)
    sorted_odd_arr = sort_arr(odd_arr)

    # Sorting could have been achieved using python inbuilt function 'sorted'. Like this - 
    # sorted_even_arr = sorted(even_arr)
    # sorted_odd_arr = sorted(odd_arr)

    # Now that we have sorted arrays we can directly get the second largest from even array and second smallest from odd array
    print("Odd array:", sorted_odd_arr)
    print("Even array: ", sorted_even_arr)

    # As the arrays are sorted in ascending order, the second largest element will be present at second last position
    # in Python we can get second last element by providing minus(-) index in array like this - 
    print("Sum : ", sorted_even_arr[-2] + sorted_odd_arr[-2])  
    

def exercise_10():
    arr = []

    size = int(input("Enter size of array:"))
    
    if size < 4:
        raise Exception("Array size must be more than or equal to 4.")
    
    for i in range(size):
        arr.append(int(input(f"Enter number for index {i}:")))
    
    print(arr)
    largeSmallSum(arr)
    

exercise_10()


