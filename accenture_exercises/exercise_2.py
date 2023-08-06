#Answers to the coding exercises in this URL - 
#https://www.codingninjas.com/studio/library/30-most-common-accenture-coding-questions


"""
2. Execute the given function.
def LargeSmallSum(arr)

The function takes an integral arr which is of the size or length of its arguments.
Return the sum of the second smallest element at odd position ‘arr’ 
and the second largest element at the even position.

Assumption

Every array element is unique.
Array is 0 indexed.
Note:

If the array is empty, return 0.
If array length is 3 or <3, return 0.
 
Example

Input:
Arr: 3 2 1 7 5 4

Output: 7 
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

    # Sort the arrays in descending order
    sorted_even_arr = sort_arr(even_arr, desc=True)
    sorted_odd_arr = sort_arr(odd_arr)

    # Sorting in descending order could have been achieved using python inbuilt function 'sorted'. Like this - 
    # sorted_even_arr = sorted(even_arr, reverse=True)
    # sorted_odd_arr = sorted(odd_arr)

    # Now that we have sorted arrays we can directly get the second largest from even array and second smallest from odd array
    print(sorted_odd_arr)
    print(sorted_even_arr)
    print("Sum : ", sorted_even_arr[1] + sorted_odd_arr[1])  
    

def exercise_2():
    arr = []

    print("Enter array elements seaparated by space:")
    inp_arr = str(input("E.g. 2 3 4 5 6 7: ")).split(" ")
    
    for inp in inp_arr:
        if inp.strip() != "":
            arr.append(int(inp))
    
    largeSmallSum(arr)
    

exercise_2()


