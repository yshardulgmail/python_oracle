"""
Given a string, the task is to reverse the order of the words in the given string. 

Examples:

Input: s = “geeks quiz practice code” 
Output: s = “code practice quiz geeks”

Input: s = “i love programming very much” 
Output: s = “much very programming love i” 
"""

def reverse_words(inp_str):
    words = inp_str.split(" ")
    print(words)
    words_length = len(words)
    output_str = ""
    for i in range(words_length - 1, -1, -1):
        output_str += words[i]

        if i != 0:
            output_str += " "

    return output_str

inp_str = str(input("Enter sentence:"))
print(reverse_words(inp_str))


