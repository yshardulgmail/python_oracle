#Answers to the coding exercises in this URL - 
#https://www.codingninjas.com/studio/library/30-most-common-accenture-coding-questions


"""
7. The given function has a string (str) and two characters, ch1 and ch2. Execute the function in such a way that str returns to its original string, and all the events in ch1 are replaced by ch2, and vice versa.
Replacecharacter(Char str1, Char ch1, Int 1, Char ch2)

Assumption

This string has only alphabets that are in lower case.

Example

Input:
str: apples
ch1: a
ch2: p

Output:
paales
"""

def Replacecharacter(ip_str, char1, char2):
    output_str = ""

    # Loop over the string chars and replace them as directed
    for ch in ip_str:
        if ch == char1:
            output_str = output_str + char2
        elif ch == char2:
            output_str = output_str + char1
        else:
            output_str = output_str + ch

    print("Output :", output_str)

def exercise_7():
    s = str(input("Enter String:"))
    c1 = str(input("Enter char1:"))
    c2 = str(input("Enter char2:"))

    
    Replacecharacter(s.lower(), c1, c2)


exercise_7()


