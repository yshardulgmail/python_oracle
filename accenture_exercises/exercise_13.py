#Answers to the coding exercises in this URL - 
#https://www.codingninjas.com/studio/library/30-most-common-accenture-coding-questions


"""
14. Change frequent character
The function to execute is
ChatFrequentcharacter(Char str, char x)

This function has a string and a character. This function requires replacing the most used character in the str with the ‘x’ character.

Note: If two characters have the same frequency, then we will have to consider the frequency which has the lower ASCII value.

Example

Input:
str: bbadbbababb
char x: t

Output:
ttadttatatt
"""


def ChatFrequentcharacter(str1, ch):
    # First create a dictionary which will have char and it's occurance count
    char_count = {}
    for c in str1:
        if c not in char_count:
            char_count[c] = 1
        else:
            char_count[c] = char_count[c] + 1

    # Now get the char who has highest number of occerances
    max_num = 0
    max_char = ""
    for c in char_count:
        # as per the problem statement if two chars have same frequency 
        # we will consider char with lower ASCII value
        if max_num == char_count[c]:
            if ord(max_char) > ord(c):
                max_char = c 
        elif max_num < char_count[c]:
            max_num = char_count[c]
            max_char = c

    # We will replace the char foun above with the once that is passed to this function
    output_str = ""
    for c in str1:
        if c == max_char:
            output_str = output_str + ch
        else:
            output_str = output_str + c

    return output_str

def exercise_13():
    str1 = input("Enter String1:")
    ch = input("Enter char:")
    
    # if string lengths are not same they are not anagrams
    if len(ch) != 1 :
        raise Exception("Enter single character to replace")
    else:
        print(ChatFrequentcharacter(str1, ch))
    

exercise_13()


