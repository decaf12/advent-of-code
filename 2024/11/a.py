from itertools import chain
from typing import List

def a(filename: str):
    lines = []
    with open(filename) as file:
        while line := file.readline():
            if line[-1] == "\n":
                lines.append(line[:-1])
            else:
                lines.append(line)
    nums = [int(num) for num in lines[0].split()]
    res = (calc(num, 75) for num in nums)
    return sum(1 for _ in chain(*res))

def calc(num: int, blinks: int):
    if not blinks:
        return [num]
    next_blinks = blinks - 1
    if not num:
        return calc(1, next_blinks)
    num_str = str(num)
    n = len(num_str)
    if not n & 1:
        half_len = n >> 1
        left_str, right_str = num_str[:half_len], num_str[half_len:]
        left, right = int(left_str), int(right_str)
        return list(chain(calc(left, next_blinks), calc(right, next_blinks)))
    return calc(num * 2024, next_blinks)


filename = "example.txt"
filename2 = "input.txt"
print(a(filename))
print(a(filename2))