#Answers to the coding exercises in this URL - 
#https://www.codingninjas.com/studio/library/30-most-common-accenture-coding-questions


"""
25. Execute a function that accepts the integer array of length ‘size’ 
and finds out the maximum number that can be formed by permutation.
Note: You will have to rearrange the numbers to make the maximum number.

Example
Input:
34 79 58 64
Output:
98765443

Explanation
All digits of the array are 3, 4, 7, 9, 5, 8, 6, and 4. The maximum number found after rearranging all the digits is 98765443.
"""

def sort_arr(arr):
    # Here i have used bubble sort to sort in descending order
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] < arr[j+1]:
                # in pythion you can swap variables like this too
                # arr[j], arr[j + 1] = arr[j + 1], arr[j]
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    
    return arr

def get_largest_number(arr):
    # first we will sort array in descending order. 
    # It will be easy to get 'k'th largest element once array sorted in descending order
    sorted_array = sort_arr(arr)
    return "".join(sorted_array)


def exercise_24():
    print("Enter array elements seaparated by space:")
    inp_arr = str(input("E.g. 2 3 4 5 6 7: ")).split(" ")
    
    # Generate single string of nummbers from the list entered above
    str_array_of_numbers = "".join(inp_arr)

    # Use list class to create list of single digits from above string
    temp_arr = list(str_array_of_numbers)
    
    # This will handle the condition in problem statement where we need to return -1 if there is no second largest number.
    if not str_array_of_numbers.isdigit():
        raise Exception("Please enter all the numbers")
    else:
        print("Output:", get_largest_number(temp_arr))
    

exercise_24()


