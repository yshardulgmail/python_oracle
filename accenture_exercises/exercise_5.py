#Answers to the coding exercises in this URL - 
#https://www.codingninjas.com/studio/library/30-most-common-accenture-coding-questions


"""
5. Perform the function for the given purpose.
For writing numbers, there is a system called N-base notation. This system uses only N-based symbols. It uses symbols that are listed as the first n symbols. Decimal and n-based notations are 0:0, 1:1, 2:2, …, 10:A, 11:B, …, 35:Z.

Perform the function: Chats DectoNBase(int n, int num)

This function only uses positive integers. Use a positive integer n and num to find out the n-base that is equal to num.

Steps

Select a decimal number and divide it by n. Consider this as an integer division.
Denote the remainder as n-based notation.
Again divide the quotient by n.
Repeat the above steps until you get a 0 remainder.
The remainders from last to first are the n-base values.
 
Assumption
1 < n < = 36

Example

Input:
N: 12
Num: 718

Output:
4BA
"""

def DectoNBase(div, num):
    output = []
    quo = num
    while quo > 0:
        # Based on problem statement we will need to separate quotient and remainder

        # This statement will give us remainder.
        output.append(quo % div)

        # This statement will give us the quotient
        quo = int(quo / div)

    # Now the tricky part. We need to assign character for the remainder values greater than 9.
    # So 10 will become A, 11 = B, 12 = C and so on.
    # We will consider ascii values to convert it into character.
    # So ASCII value of A is 65, B = 66 and so on. 
    # So we will add 55 to the remainder values which are greater than 9
    # E.g If remainder is 14. Adding 55 to it will become 69 which is ASCII value of 'E'
    final_output = ""
    for op in reversed(output):
        if op > 9:
            final_output += chr(op+55)
        else:
            final_output += str(op)

    print("Output:", final_output)


def exercise_5():
    d = int(input("Enter divider:"))
    n = int(input("Enter number:"))

    # The condition is mentioned in problem statement that divider need to be <= 36
    if d <= 0 or n <= 0 or d > 36:
        raise Exception("Please enter non zero positive numbers.")
    
    DectoNBase(d, n)


exercise_5()


