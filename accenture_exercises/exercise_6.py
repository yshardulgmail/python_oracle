#Answers to the coding exercises in this URL - 
#https://www.codingninjas.com/studio/library/30-most-common-accenture-coding-questions


"""
6. Execute the function for the given purpose.
When the sum of the digits exceeds a total of 9, a carry digit is added to the right-left of the digit. Execute the function: Int Numberofcarry(Integer num 1, Integer num 2)

Assumption

num1, num2 > = 0

Example

Input:
num1: 451
num2: 349

Output:
2
"""

def Numberofcarry(num1, num2):
    # As we care about the sum of individual digits in numbers 
    # and not the sum of 2 whole numbers we will convert them into strings
    str_num1 = str(num1)
    str_num2 = str(num2)

    # Declare var which will be summation of caries
    total_carry = 0

    # This will act as a carry value to next sum
    carry = 0

    # if length of numbers is not same we will add zeros to the left of smaller number
    if len(str_num1) < len(str_num2):
        str_num1 = str_num1.rjust(len(str_num2), "0")
    else:
        str_num2 = str_num2.rjust(len(str_num1), "0")
    
    
    # Now as the addition of numbers happen from right to left we will traverse the array in reverse
    # Please do read 'range()' function in python. it is very handy.

    for i in range(len(str_num1) - 1, -1, -1):
        if (int(str_num1[i]) + int(str_num2[i]) + carry) > 9:
            total_carry = total_carry + 1
            carry = 1
        else:
            carry = 0

    return total_carry
 

def exercise_6():
    n1 = int(input("Enter Num1:"))
    n2 = int(input("Enter Num2:"))

    if n1 <= 0 or n2 <= 0:
        raise Exception("Please enter non zero positive numbers.")
    
    print("Output :", Numberofcarry(n1, n2))


exercise_6()


