def sort_arr(arr):
    # Here i have used bubble sort to sort in descending order
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                # in pythion you can swap variables like this too
                # arr[j], arr[j + 1] = arr[j + 1], arr[j]
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
         
    return arr

candidates = input()

if not candidates.isdigit():
    raise Exception("Batch must be number")

candidates = int(candidates)
marks_str = input()
marks = []
for mark in marks_str.split(" "):
    if not mark.isdigit():
        raise Exception("marks must be number")
    else:
        marks.append(int(mark))

if len(marks) != candidates:
    raise Exception("Enter correct no. of marks")

lower_limit = int(input(""))
higher_limit = int(input(""))

marks = sort_arr(marks)
print(marks)
marks_cnt = 0
from_range = 0
to_range = lower_limit
ranges = []
last_found = 0
first = True
for i in range(lower_limit, higher_limit+1):
    if i == marks[marks_cnt]:
        print(last_found)
        if last_found == lower_limit:
            from_range = lower_limit
        else:
            from_range = last_found + 1            
        to_range = i - 1
        if from_range == to_range:
            ranges.append(from_range)
        else:
            ranges.append("%d->%d" % (from_range, to_range))
            
        last_found = i  
        marks_cnt += 1
        if marks_cnt == len(marks):
            marks_cnt -= 1

ranges.append("%d->%d" % (last_found + 1, higher_limit))
print(ranges)