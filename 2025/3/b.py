from collections import deque
from itertools import accumulate, count
from typing import List

def uniq(nums: List[int]):
    n = len(nums)
    stack = deque()
    for pos, num in enumerate(nums):
        remaining_digits = n - pos
        while stack and len(stack) + remaining_digits > 12 and stack[-1] < num:
            stack.pop()
        if len(stack) < 12:
            stack.append(num)
    return int("".join(str(digit) for digit in stack))

def b(filename: str):
    res = 0
    with open(filename) as file:
        while line := file.readline():
            if line[-1] == '\n':
                line = line[:-1]
            line = [int(digit) for digit in line]
            subtotal = uniq(line)
            res += subtotal
    return res

print(b('./example.txt'))
print(b('./input.txt'))