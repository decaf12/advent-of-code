from functools import cache
from itertools import chain
from typing import List

def b(filename: str):
    lines = []
    with open(filename) as file:
        while line := file.readline():
            if line[-1] == "\n":
                lines.append(line[:-1])
            else:
                lines.append(line)
    nums = [int(num) for num in lines[0].split()]
    return sum(calc2(num, 75) for num in nums)

@cache
def calc2(num: int, blinks: int):
    if not blinks:
        return 1
    if num < 10:
        stat = stats[num]
        max_blink = len(stat) - 1
        if blinks < max_blink:
            return len(stat[blinks])
        next_blinks = blinks - max_blink
        return sum(calc2(num, next_blinks) for num in stat[-1])
    next_blinks = blinks - 1
    num_str = str(num)
    n = len(num_str)
    if not n & 1:
        half_len = n >> 1
        left_str, right_str = num_str[:half_len], num_str[half_len:]
        left, right = int(left_str), int(right_str)
        return calc2(left, next_blinks) + calc2(right, next_blinks)
    return calc2(num * 2024, next_blinks)

stats = [
    [[0], [1], [2024], [20, 24], [2, 0, 2, 4]],
    [[1], [2024], [20, 24], [2, 0, 2, 4]],
    [[2], [4048], [40, 48], [4, 0, 4, 8]],
    [[3], [6072], [60, 72], [6, 0, 7, 2]],
    [[4], [8096], [80, 96], [8, 0, 9, 6]],
    [[5], [10120], [20482880], [2048, 2880], [20, 48, 28, 80], [2,0,4,8,2,8,8,0]],
    [[6], [12144], [24579456], [2457, 9456], [24, 57, 94, 56], [2,4,5,7,9,4,5,6]],
    [[7], [14168], [28676032], [2867, 6032], [28, 67, 60, 32], [2,8,6,7,6,0,3,2]],
    [[8], [16192], [32772608], [3277, 2608], [32, 77, 26, 8]],
    [[9], [18216], [36869184], [3686, 9184], [36, 86, 91, 84], [3,6,8,6,9,1,8,4]],
]

filename = "example.txt"
filename2 = "input.txt"
print(b(filename))
print(b(filename2))