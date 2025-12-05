from collections import deque
from math import inf
from typing import List

def merge_intervals(intervals: List[List[int]]):
    intervals.sort()
    res = []
    for start, end in intervals:
        if res:
            prev_end = res[-1][1]
            if start > prev_end:
                res.append([start, end])
            else:
                res[-1][1] = max(prev_end, end)
        else:
            res.append([start, end])
    return res

def b(filename: str):
    intervals = []
    with open(filename) as file:
        while line := file.readline().rstrip():
            start, end = map(int, line.split('-'))
            intervals.append((start, end))
        
    merged_intervals = merge_intervals(intervals)
    return sum(end - start + 1 for start, end in merged_intervals)

print(b('./example.txt'))
print(b('./input.txt'))