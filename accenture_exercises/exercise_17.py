#Answers to the coding exercises in this URL - 
#https://www.codingninjas.com/studio/library/30-most-common-accenture-coding-questions


"""
18. Create web access management to the kth largest number. 
It will accept an integer k and an array arr as its conditions and has 
to return the greatest element based on the value of k. 
That is, if k = 0, return the greatest element. 
If k = 1, return the second greatest element, and so on.
Example

Suppose the array contains values like {74, 85, 102, 99, 101, 56, 84} 
and the integer k is 2. The method will return 99, the third greatest element, 
as there are only two (according to the value of k) values greater than 99 (101 and 102).
"""

def sort_arr(arr):
    # Here i have used bubble sort to sort in descending order
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] < arr[j + 1]:
                # in pythion you can swap variables like this too
                # arr[j], arr[j + 1] = arr[j + 1], arr[j]
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
         
    return arr

def get_largest(arr, k):
    # first we will sort array in descending order. 
    # It will be easy to get 'k'th largest element once array sorted in descending order
    sorted_array = sort_arr(arr)
    return sorted_array[k] 


def exercise_17():
    # we will use set here to avoid duplicates and get the 'k'th largest number correctly.
    # e.g. in this scenario where,
    # arr = [2,1,2] , AND
    # k = 1
    # sorting the array will give us [2, 2, 1] 
    # and if we try to return 1st element from array it will return 2 and it will be a wrong answer.

    temp_arr = set()
    k = int(input("Enter value of k:"))
    print("Enter array elements seaparated by space:")
    inp_arr = str(input("E.g. 2 3 4 5 6 7: ")).split(" ")
    
    for inp in inp_arr:
        if inp.strip() != "":
            temp_arr.add(int(inp))

    # convert it back to list so that we can traverse it using loops. Sets in python cannot be traversed using index.
    # E.g. if temp_arr is set you cannot do 'temp_arr[2]'. 
    temp_arr = list(temp_arr)

    if len(temp_arr) < k:
        raise Exception("Cannot get kth value from the array. It length is shorter.")

    print("Output:", get_largest(temp_arr, k))
    

exercise_17()


