#Answers to the coding exercises in this URL - 
#https://www.codingninjas.com/studio/library/30-most-common-accenture-coding-questions


"""
3. Write a function to validate if the provided two strings are anagrams or not. 
If the two strings are anagrams, then return ‘yes’. Otherwise, return ‘no’.
Input:

Input 1: 1st string
Input 2: 2nd string

Output:
(If they are anagrams, the function will return ‘yes’. Otherwise, it will return ‘no’.)

Example

Input 1: Listen
Input 2: Silent

Output:
Yes 
"""

def is_anagram(str1, str2):
    for ch in str1:
        # if any of the character from string 1 is not present in string 2 they are not anagrams
        if ch not in str2:
            return "No"
    
    return "Yes"

def exercise_3():
    str1 = input("Enter String1:")
    str2 = input("Enter String2:")

    # if string lengths are not same they are not anagrams
    if len(str1) != len(str2):
        print("No")
    else:
        print(is_anagram(str1, str2))
    

exercise_3()


