#Answers to the coding exercises in this URL - 
#https://www.codingninjas.com/studio/library/30-most-common-accenture-coding-questions


"""
8. Perform the function: Int operationchoices(int c, int n, int a, int b). This function considers three positive inputs of a, b and c.
Execute the function to get:
(a + b), if c = 1
(a / b), if c = 4
(a – b), if c = 2
(a x b), if c = 3

Example:

Input:
a: 12
b: 16
c: 1

Output:
28
"""

def operationchoices(num1, num2, op):
    if op == 1:
        return num1 + num2
    if op == 2:
        return num1 - num2
    if op == 3:
        return num1 * num2
    if op == 4:
        return num1 / num2

 

def exercise_8():
    n1 = int(input("Enter Num1:"))
    n2 = int(input("Enter Num2:"))
    print("Enter operation num:")
    op = int(input("1 = +, 2 = -, 3 = x, 4 = / :"))

    
    print("Output :", operationchoices(n1, n2, op))


exercise_8()


