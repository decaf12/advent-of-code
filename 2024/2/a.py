from itertools import pairwise
from typing import List


def a(filename: str):
    res = 0
    with open(filename) as file:
        while line := file.readline():
            nums = [int(token) for token in line.split()]
            if is_good(nums):
                res += 1
    return res

def is_good(nums: List[int]):
    n = len(nums)
    if n == 1:
        return True
    if nums[1] == nums[0]:
        return False
    is_increasing = nums[1] > nums[0]
    for prev, curr in pairwise(nums):
        if is_increasing:
            if curr <= prev:
                return False
        elif curr >= prev:
            return False
        diff = curr - prev
        if diff < 0:
            diff = -diff
        if diff not in range(1, 4):
            return False
    return True

print(a('./example.txt'))
print(a('./input.txt'))