#Answers to the coding exercises in this URL - 
#https://www.codingninjas.com/studio/library/30-most-common-accenture-coding-questions


"""
29. Write a function to find if the given string is a palindrome or not. 
Return 1 if the input string is a palindrome, else return 0.
Input:
level
Output:
1

Explanation:
The reverse of the string ‘level’ is ‘level’. As they are the same, the string is a palindrome.
"""

def palindrome(str1):
    str_array = list(str1)
    length = len(str_array)
    limit = int(length / 2)
    for i in range(limit):
        if str_array[i] != str_array[length - 1 - i]:
            return 0
        
    return 1


def exercise_25():
    str1 = input("Enter string:")
    
    print("Output:", palindrome(str1))
    

exercise_25()


