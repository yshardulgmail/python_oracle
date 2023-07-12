#Answers to the coding exercises in this URL - 
#https://www.codingninjas.com/studio/library/30-most-common-accenture-coding-questions


"""
26. Find a string of a length of 1000 for a large number.
Output is the modulo of 11. The output specification is 
to return the remainder modulo 11 of the input.

Input:
121
Output:
0

Explanation
121 mod 11 = 0
"""

def exercise_25():
    num = int(input("Enter number:"))
    
    if num < 1:
        raise Exception("Number must be more than 0.")
    else:
        print("Output:", num % 11)
    

exercise_25()


