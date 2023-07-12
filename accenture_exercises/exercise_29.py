#Answers to the coding exercises in this URL - 
#https://www.codingninjas.com/studio/library/30-most-common-accenture-coding-questions


"""
30. Write a function to check if the given two strings are anagrams or not. 
Return ‘Yes’ if they are anagrams, otherwise, return ‘No’.
Example
Input 1: build
Input 2: dubli
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


