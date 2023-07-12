#Answers to the coding exercises in this URL - 
#https://www.codingninjas.com/studio/library/30-most-common-accenture-coding-questions


"""
16. In a given list of integers, find the number that has the highest frequency. If there are one or more such numbers, give the smaller one as output.
Input:
3
7
2 4 5 2 3 2 4
6
1 2 1 1 2 1
10
1 1 1 1 1 1 1 1 1 1

Output:
2
1
1
"""

def find_count(arr):
    num_count = {}
    for a in arr:
        if a not in num_count:
            num_count[a] = 1
        else:
            num_count[a] = num_count[a] + 1

    return num_count

def find_max_count(num_count):
    # Now get the char who has highest number of occerances
    max_count = 0
    max_num = ""
    for c in num_count:
        # as per the problem statement if two chars have same frequency 
        # we will consider char with lower ASCII value
        if max_count == num_count[c]:
            if max_num > c:
                max_num = c 
        elif max_count < num_count[c]:
            max_count = num_count[c]
            max_num = c

    return max_num

def find_frequency(arr):
    for array in arr:
        num_count = find_count(array)

        print("Max number: ", find_max_count(num_count))


def exercise_15():
    arr = []

    count = int(input("Enter no. of arrays you are going to provide:"))

    for i in range(count):
        temp_arr = []
        length = int(input("Enter length of array: "))
        print("Enter array elements seaparated by space:")
        inp_arr = str(input("E.g. 2 3 4 5 6 7: ")).split(" ")
        
        arr.append(inp_arr)
    
    find_frequency(arr)
    

exercise_15()


