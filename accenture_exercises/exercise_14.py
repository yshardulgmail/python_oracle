#Answers to the coding exercises in this URL - 
#https://www.codingninjas.com/studio/library/30-most-common-accenture-coding-questions


"""
15. Execute the function Def Autocount(n).
The function accepts the string n. It checks whether the number is an autobiographical number or not. 
If an integer returns, then it is an autobiographical number. 
If 0 returns, then it is not an autobiographical number.

Assumption

The input value should not be more than 10 characters.
The input string will have numeric characters.
 
Example

Input:
N: “1210”

Output:
3
"""

def get_char_count(str1, ch):
    count = 0
    for c in str1:
        if ch == c:
            count += 1

    return count


def Autocount(str1):
    """
    In simple terms, if the given number’s digits from left to right represent 
    the frequency of 0, 1, 2, 3, 4.... N respectively present in the given number 
    then that number is known as Autobiographical number.
    Some examples of Autobiographical numbers are: 1210, 2020, 21200, 3211000, 42101000 ... etc.

    Input number is 1210.
    Let’s check it by using the logic of Autobiographical numbers.
    Number of zeros available in the given number is = 1. And the first digit is also 1.
    Number of one’s available in the given number is= 2. And the second digit is also 2.
    Number of two available in the given number is= 1. And the third digit is also 1.
    Number of three’s available in the given number is= 0. And the fourth digit is also 0.
    As we notice here by arranging all those digits, we will get the same original number.
    Hence, 1210 is an Autobiographical number.
    """
    for i in range(len(str1)):
        if int(str1[i]) != get_char_count(str1, str(i)):
            return 0
        
    return len(str1) - 1

def exercise_14():
    str1 = input("Enter String:")
    
    # if string lengths are not same they are not anagrams
    if len(str1) > 10 or not str1.isdigit():
        raise Exception("Length of numbers should not exceed 10 and it should contain all numbers.")
    else:
        print(Autocount(str1))
    

exercise_14()


