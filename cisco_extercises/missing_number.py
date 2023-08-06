def findMissing(arr, N):
    for i in range(1, N+1):
        if i not in arr:
            print("Missing No.:", i)
            break


# Driver code
if __name__ == '__main__':
    arr = [1, 2, 3, 5]
    N = len(arr)
 
    # Function call
    findMissing(arr, N)