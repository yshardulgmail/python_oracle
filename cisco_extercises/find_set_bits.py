"""
Write an efficient program to count the number of 1s in the binary representation of an integer.
Examples : 

Input : n = 6
Output : 2
Binary representation of 6 is 110 and has 2 set bits

Input : n = 13
Output : 3
Binary representation of 13 is 1101 and has 3 set bits
"""


def count_set_bits(n):
    count = 0
    while (n):
        print("n =", n)
        print("count before =", count)

        count += n & 1
        print("count after =", count)
        n >>= 1
    return count
 

i = 13
# 1101
print(count_set_bits(i))