#Answers to the coding exercises in this URL - 
#https://www.codingninjas.com/studio/library/30-most-common-accenture-coding-questions


"""
13. Execute this function Void MaxInArray(int arr[], int length)
This function helps in finding the maximum element in the array. Execute this function to print the maximum element in the array with its index.

Assumptions

The index in the array for all the elements starts at 0.
The maximum element is in a different line in the output.
There has to be only one maximum element.
The function prints only what is required.
 
Example

Input:
23 45 82 27 66 12 78 13 71 86

Output:
86
9
"""

def MaxInArray(arr):
    max_num = arr[0]
    max_index = 0
    for i in range(1, len(arr)):
        if arr[i] > max_num:
            max_num = arr[i]
            max_index = i

    print("Max number: ", max_num)
    print("Max number index: ", max_index)

def exercise_12():
    arr = []

    print("Enter array elements seaparated by space:")
    inp_arr = str(input("E.g. 2 3 4 5 6 7: ")).split(" ")
    
    for inp in inp_arr:
        if inp.strip() != "":
            arr.append(int(inp))
    
    MaxInArray(arr)
    

exercise_12()


