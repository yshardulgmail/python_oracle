#Answers to the coding exercises in this URL - 
#https://www.codingninjas.com/studio/library/30-most-common-accenture-coding-questions


"""
23. Perform a function to reverse a string word-wise. 
The input here will be the string. In the output, 
the last word mentioned should come as the first word and vice versa.
Example
Input:
Welcome to code
Output:
code to Welcome
"""

def print_in_reverse(arr):
    # This for loop will help to traverse in reverse order
    for i in range(len(arr) - 1, -1, -1):
        print(arr[i], end=" ")

    print("")

def exercise_22():
    inp_arr = str(input("Enter list of words:")).split(" ")
    
    print_in_reverse(inp_arr)
    

exercise_22()


