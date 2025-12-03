from collections import deque
from itertools import accumulate, count, pairwise

def a(filename: str):
    res = 0
    with open(filename) as file:
        while line := file.readline():
            line = [int(digit) for digit in line[:-1]]
            n = len(line)
            left = [0] * n
            right = [0] * n
            max_left = 0
            max_right = 0

            for pos, digit in enumerate(line):
                max_left = max(digit, max_left)
                left[pos] = max_left
            
            for pos in range(n - 1, -1, -1):
                max_right = max(line[pos], max_right)
                right[pos] = max_right
            
            subtotal = 0
            for lp, rp in pairwise(range(n)):
                left_max = left[lp]
                right_max = right[rp]
                subtotal = max(subtotal, left_max * 10 + right_max)
            res += subtotal
    return res

print(a('./example.txt'))
print(a('./input.txt'))