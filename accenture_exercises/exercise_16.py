#Answers to the coding exercises in this URL - 
#https://www.codingninjas.com/studio/library/30-most-common-accenture-coding-questions


"""
17. Execute the function for the given purpose.
Write a function mergeArrays which merges two sorted arrays to create one single sorted array.
 Complete the function int* mergeArrays(int a[], int b[], int asize, int bsize) 
 below which takes the pointers to the first element of the two sorted arrays and the size of the arrays, 
 and returns the base address of the final sorted array.

Input:
4 // Size of 1st array
1 2 3 6 // Elements of 1st array
3 // Size of 2nd array
4 5 7 // Elements of 2nd array

Output:
1
2
3
4
5
6
7
"""

def sort_arr(arr):
    # Here i have used bubble sort
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1]:
                # in pythion you can swap variables like this too
                # arr[j], arr[j + 1] = arr[j + 1], arr[j]
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
         
    return arr

def merge_arrays(arr1, arr2):
    arr = []
    for a in arr1:
        arr.append(a)

    for a in arr2:
        arr.append(a)

    # Above could have achieved like this too
    # arr.append(arr1)
    # arr.append(arr2)

    return sort_arr(arr) 


def exercise_16():
    arr = []

    for i in range(2):
        temp_arr = []
        length = int(input("Enter length of array: "))
        print("Enter array elements seaparated by space:")
        inp_arr = str(input("E.g. 2 3 4 5 6 7: ")).split(" ")
        
        for inp in inp_arr:
            if inp.strip() != "":
                temp_arr.append(int(inp))
        arr.append(temp_arr)
    
    print(merge_arrays(arr[0], arr[1]))
    

exercise_16()


