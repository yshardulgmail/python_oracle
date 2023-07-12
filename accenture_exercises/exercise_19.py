#Answers to the coding exercises in this URL - 
#https://www.codingninjas.com/studio/library/30-most-common-accenture-coding-questions


"""
20. Write a program to count the number of swaps required to sort a given list of integers 
in ascending order using the selection sort algorithm.
Input:
2
3
4 2 5
5
10 11 8 7 1

Output:
1
3
"""

def get_swap_count(arr):
    # Here i have used selection sort
    n = len(arr)
    swap_count = 0
    
    for i in range(n):
        index_changed = False
        min_index = i
 
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
                index_changed = True

        if index_changed:
            temp = arr[i]
            arr[i] = arr[min_index]
            arr[min_index] = temp

            swap_count = swap_count + 1

    print(arr)
         
    return swap_count

def find_frequency(arr):
    for array in arr:
        print("Swap count: ", get_swap_count(array))


def exercise_19():
    arr = []

    count = int(input("Enter no. of arrays you are going to provide:"))

    for i in range(count):
        temp_arr = []
        length = int(input("Enter length of array: "))
        print("Enter array elements seaparated by space:")
        inp_arr = str(input("E.g. 2 3 4 5 6 7: ")).split(" ")
        for inp in inp_arr:
            if inp.strip() != "":
                temp_arr.append(int(inp))
        
        arr.append(temp_arr)
    
    find_frequency(arr)
    

exercise_19()


