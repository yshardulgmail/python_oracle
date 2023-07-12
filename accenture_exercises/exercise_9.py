#Answers to the coding exercises in this URL - 
#https://www.codingninjas.com/studio/library/30-most-common-accenture-coding-questions


"""
9. Perform the function Int calculate(int m, int n). This function needs two positive integers. 
Calculate the sum of numbers between these two numbers that are divisible by 3 and 5.
Assumption
m > n > = 0

Example

Input:
m: 12
n: 50

Output:
90

Explanation
The numbers between 12 and 50 that are divisible by 3 and 5 are 15, 30, and 45. The sum of these numbers is 90.

Sample input:
m: 100
n: 160

Sample output:
405
"""

def calculate(num1, num2):
    # we need to check every number between the limits specified.
    # So we will initiallize our counters with lowest number and highest numbers

    start = 0
    end = 0
    if num1 < num2:
        start = num1
        end = num2
    else:
        start = num2
        end = num1

    sum = 0
    while start <= end:
        if (start % 3 == 0) and (start % 5 == 0):
           sum += start

        start += 1 

    return sum
 

def exercise_9():
    n1 = int(input("Enter Num1:"))
    n2 = int(input("Enter Num2:"))

    if n1 < 0 or n2 < 0:
        raise Exception("Please enter non zero positive numbers.")
    
    print("Output :", calculate(n1, n2))


exercise_9()


