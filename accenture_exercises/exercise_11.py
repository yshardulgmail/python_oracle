#Answers to the coding exercises in this URL - 
#https://www.codingninjas.com/studio/library/30-most-common-accenture-coding-questions


# I DID NOT UNDERSTAND PROBLEM STATEMENT OF EXERCISE 11. IN ABOVE LINK. SO I AM RESUMING FROM 12TH.

"""
12. Perform the function Checkpassword (char str[], int n)
Execute the function which happens to be 1 if the str is a valid password or it remains 0.

Conditions for a valid password: 

The password should have at least 4 characters.
It should have at least 1 digit.
It should have one capital letter.
It should not have any spaces or obliques (/).
The first character should not be a number.
 
Assumption
The input is not empty.

Example

Input:
aA1_67

Output:
1 
"""

def contains_digit(str1):
    for ch in str1:
        if ch.isdigit():
            return 1

    return 0


def contains_upper(str1):
    for ch in str1:
        if ch.isupper():
            return 1

    return 0


def Checkpassword(str1):
    ret_num = 0
    if str1[0].isdigit():
        return 0
    elif "/" in str1 or " " in str1:
        return 0
    elif contains_digit(str1) == 0 or contains_upper(str1) == 0:
        return 0

    return 1

def exercise_11():
    str1 = input("Enter String1:")
    
    # if string lengths are not same they are not anagrams
    if len(str1) < 4 :
        print("Output:", 0)
    else:
        print(Checkpassword(str1))
    

exercise_11()


