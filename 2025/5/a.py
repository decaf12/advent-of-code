from bisect import bisect_left
from heapq import merge
from operator import itemgetter
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

def is_fresh(num: int, intervals: List[List[int]]):
    n = len(intervals)
    pos = bisect_left(intervals, num, key=itemgetter(1))
    if pos == n:
        return False
    start, _ = intervals[pos]
    return start <= num

def a(filename: str):
    intervals = []
    res = 0
    with open(filename) as file:
        while line := file.readline().rstrip():
            start, end = map(int, line.split('-'))
            intervals.append((start, end))
        
        merged_intervals = merge_intervals(intervals)
        while line := file.readline().rstrip():
            num = int(line)
            if is_fresh(num, merged_intervals):
                res += 1
    return res

print(a('./example.txt'))
print(a('./input.txt'))