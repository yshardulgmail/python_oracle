#Answers to the coding exercises in this URL - 
#https://www.codingninjas.com/studio/library/30-most-common-accenture-coding-questions


"""
24. Find the sum of the divisors for the N integer number.

Example 1
Input:
6
Output:
12
"""

def sum_of_divisors(num):
    total = 0
    for i in range(1, num+1):
        if num % i == 0:
            total = total + i
        
    return total

def exercise_23():
    num = int(input("Enter number:"))
    
    if num < 1:
        raise Exception("Number must be more than 0.")
    else:
        print(sum_of_divisors(num))
    

exercise_23()


