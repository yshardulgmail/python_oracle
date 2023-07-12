#Answers to the coding exercises in this URL - 
#https://www.codingninjas.com/studio/library/30-most-common-accenture-coding-questions

import math

"""
28. Write a function to find roots of a quadratic equation ax^2 + bx + c = 0.
Note: The formula to find the roots of a quadratic equation is given below:

Example
Input 1: 1
Input 2: –2
Input 3: 3
Output:
{3.0,–1.0}

Explanation:
On substituting the values of a, b, and c in the formula, the roots will be as follows:
+X = 3.0
-X = –1.0
"""

def get_roots(a, b, c):
    # Formulae for getting roots of quadratic equation
    # +X = (-b + sqrt(b*b - 4ac)) / 2a
    # -X = (-b - sqrt(b*b - 4ac)) / 2a 

    sqrt_formula = abs((b * b) - (4 * a * c))
    print(sqrt_formula)
    root1 = (-b + math.sqrt(sqrt_formula)) / (2 * a)
    root2 = (-b - math.sqrt(sqrt_formula)) / (2 * a)

    return [float(math.ceil(root1)), -float((math.ceil(-root2)))]

def exercise_27():
    a = int(input("Enter number:"))
    b = int(input("Enter number:"))
    c = int(input("Enter number:"))
    
    print(a, b, c)
    print("Output:", get_roots(a, b, c))
    

exercise_27()


