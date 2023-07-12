#Answers to the coding exercises in this URL - 
#https://www.codingninjas.com/studio/library/30-most-common-accenture-coding-questions


"""
22. Adam decides to do some charity work. From day 1 till day n, 
he will give i^2 coins to charity. On day ‘i’ (1 < = i < = n), 
find the number of coins he gives to charity.

Example 1
Input:
2
Output:
5
Explanation:
There are 2 days.
Example 2

Input:
3

Output:
14
"""

def get_char_count(str1, ch):
    count = 0
    for c in str1:
        if ch == c:
            count += 1

    return count


def charity(days):
    total_charity = 0
    for i in range(1, days+1):
        total_charity += (i * i)
        
    return total_charity

def exercise_21():
    days = int(input("Enter no. of days:"))
    
    if days < 1:
        raise Exception("No of days must be more than 0.")
    else:
        print(charity(days))
    

exercise_21()


