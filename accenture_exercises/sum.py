import math
import sys


def get_sum(N):
    try:
        int("aaa")
    except ValueError as e:
        print("I know its value error")
    except Exception as e:
        print("Need to exit")
        sys.exit(0)

    sum = 0
    while N:
        sum += N % 10
        N //= 10

    if len(str(sum)) > 1:
        return get_sum(sum)
    else:
        return sum
    

def solve(N):
    powered_num = int(math.pow(2, N))

    try:
        return get_sum(powered_num)
    except ValueError as e:
        print(type(e))
        print("ValueError:", e)
    except Exception as e:
        print(type(e))
        print("Exception:", e)

T = int(input())
if T < 1 or T > 100000:
    raise Exception("Error!!!")

for _ in range(T):
    N = int(input())   
    out_ = solve(N)
    print(out_)