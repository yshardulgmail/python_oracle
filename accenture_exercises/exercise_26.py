#Answers to the coding exercises in this URL - 
#https://www.codingninjas.com/studio/library/30-most-common-accenture-coding-questions


"""
27. Find out if the given set of points are on a straight line or not. 
If the points are on a straight line, then return the equation. If not, then return 0.

Example
Input:
3
1 1 2 2 3 3
Output:
1x – 1y = 0

Explanation
The three points here are [1,1], [2,2], and [3,3]. These lie on a line, so the function returned the equation.
"""

def check_straight_line(arr):
    for point in arr:
        if (point[0] - point[1]) != 0:
            return 0
        
    return "1x – 1y = 0"


def exercise_26():
    points = int(input("Enter no. of points:"))
    print("Enter point coordinates:")
    inp_arr = str(input("E.g. 1 1 2 2: ")).split(" ")
    
    # Generate array of [x,y] points
    temp_arr = []
    first = None
    second = None
    for e in inp_arr:
        if not first:
            first = int(e)
        elif not second:
            second = int(e)
            temp_arr.append([first, second])
            first = second = None

    print(temp_arr)
    # This will handle the condition in problem statement where we need to return -1 if there is no second largest number.
    if len(temp_arr) != points:
        raise Exception("Please same number points as mentioned")
    else:
        print("Output:", check_straight_line(temp_arr))
    

exercise_26()


