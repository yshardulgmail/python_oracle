#Answers to the coding exercises in this URL - 
#https://www.codingninjas.com/studio/library/30-most-common-accenture-coding-questions


"""
1. Execute the given function.
def differenceofSum(n.m)

The function takes two integrals m and n as arguments. 
You are required to obtain the total of all integers ranging between 1 to n (both inclusive) which are not divisible by m. 
You must also return the distinction between the sum of integers not divisible by m with the sum of integers divisible by m.

Assumption

m > 0 and n > 0
Sum lies within the integral range 

Example
Input:
m = 6
n = 30

Output:
285
"""

def differenceofSum(n, m):
    sum1 = 0
    sum2 = 0

    i=1
    while i <= n: 
        if (i % m) == 0:
            print("divisible ", i)
            sum1 = sum1 + i
        else:
            print("not divisible ", i)
            sum2 = sum2 + i
        i = i + 1

    print("Difference of sum is - ", sum2 - sum1)


def exercise_1():
    n = int(input("Enter value for n:"))
    m = int(input("Enter value for m:"))

    if n <= 0 or m <= 0:
        raise Exception("Please enter non zero positive numbers.")
    
    differenceofSum(n, m)


exercise_1()


