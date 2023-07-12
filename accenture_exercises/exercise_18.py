#Answers to the coding exercises in this URL - 
#https://www.codingninjas.com/studio/library/30-most-common-accenture-coding-questions


"""
19. We have mentioned a list of integers that have no duplicates. 
Find how many swaps it will take to sort the list in ascending order using Bubble sort.
Input:
3
5
2 1 4 6 3
10
123 21 34 45 25 675 23 44 55 900
1
23

Output:
3
16
0
"""

def get_swap_count(arr):
    # Here i have used bubble sort
    n = len(arr)
    # we will count the swaps with this
    swap_count = 0
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1]:
                # in python you can swap variables like this too
                # arr[j], arr[j + 1] = arr[j + 1], arr[j]
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
                swap_count = swap_count + 1

    print(arr)
         
    return swap_count

def find_frequency(arr):
    for array in arr:
        print("Swap count: ", get_swap_count(array))


def exercise_18():
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
    

exercise_18()


