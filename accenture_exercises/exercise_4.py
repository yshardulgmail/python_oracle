#Answers to the coding exercises in this URL - 
#https://www.codingninjas.com/studio/library/30-most-common-accenture-coding-questions


"""
4. Perform the following function. 
def Productsmallpair(sum,arr)

This function accepts the integers sum and arr. 
It is used to find the arr(j) and arr(k), where k ! = j. arr(j) and arr(k) should be the smallest elements in the array.

Keep this in mind:

If n<2 or empty, return –1.
If these pairs are not found, then return to zero.
Make sure all the values are within the integer range.
 
Example

Input:
Sum: 9
Arr: 5 4 2 3 9 1 7

Output:
2 
"""

def productsmallpair(sum, arr):
    # Using python in built function 'sorted' here. 
    sorted_arr = sorted(arr)

    for i in range(len(sorted_arr) - 1):
        if (sorted_arr[i] + sorted_arr[i+1]) < sum:
            print("Output: ", sorted_arr[i] * sorted_arr[i+1])

def exercise_4():
    arr = []

    sum = int(input("Enter sum: "))
    print("Enter array elements seaparated by space:")
    inp_arr = str(input("E.g. 2 3 4 5 6 7: ")).split(" ")
    
    for inp in inp_arr:
        if inp.strip() != "":
            arr.append(int(inp))
    
    productsmallpair(sum, arr)
    

exercise_4()


