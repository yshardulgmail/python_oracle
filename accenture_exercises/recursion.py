

def recursion(val):
    if val == 5:
        return val
    else:
        print("Value : ", val)
        return val * recursion(val+1)
    
if __name__ == "__main__":
    # 1 * 2 * 3 * 4 * 5
    print(recursion(1))