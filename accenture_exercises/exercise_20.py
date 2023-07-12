#Answers to the coding exercises in this URL - 
#https://www.codingninjas.com/studio/library/30-most-common-accenture-coding-questions


"""
21. Form an array of 1000 integers and find out the second-largest number. 
If there is no second largest number, return the value to –1.
Example
Input 1:
3
Input 2:
{2,1,2}
Output:
1
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

def get_second_largest(arr):
    # first we will sort array in descending order. 
    # It will be easy to get 'k'th largest element once array sorted in descending order
    sorted_array = sort_arr(arr)
    return sorted_array[1] 


def exercise_20():
    temp_arr = set()
    print("Enter array elements seaparated by space:")
    inp_arr = str(input("E.g. 2 3 4 5 6 7: ")).split(" ")
    
    for inp in inp_arr:
        if inp.strip() != "":
            temp_arr.add(int(inp))
    
    # convert it back to list so that we can traverse it using loops. Sets in python cannot be traversed using index.
    # E.g. if temp_arr is set you cannot do 'temp_arr[2]'. 
    temp_arr = list(temp_arr)
    
    # This will handle the condition in problem statement where we need to return -1 if there is no second largest number.
    if len(temp_arr) < 2:
        print("Output:", -1)
    else:
        print("Output:", get_second_largest(temp_arr))
    

exercise_20()


