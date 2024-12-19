from collections import deque
from typing import List

def a(filename: str):
    lines = []
    with open(filename) as file:
        while line := file.readline():
            if line[-1] == "\n":
                line = line[:-1]
            lines.append([int(digit) for digit in line])
    return process(lines)

def process(graph: List[List[int]]):
    height, width = len(graph), len(graph[0])
    def neighbours(rownum: int, colnum: int):
        if rownum:
            yield rownum - 1, colnum
        if rownum < height - 1:
            yield rownum + 1, colnum
        if colnum:
            yield rownum, colnum - 1
        if colnum < width - 1:
            yield rownum, colnum + 1

    def count_score(start_row: int, start_col: int):
        stack = deque([(start_row, start_col)])
        res = 0
        while stack:
            curr_row, curr_col = stack.pop()
            curr_height = graph[curr_row][curr_col]
            if curr_height == 9:
                res += 1
            else:
                target_height = curr_height + 1
                for next_row, next_col in neighbours(curr_row, curr_col):
                    next_height = graph[next_row][next_col]
                    if next_height != target_height:
                        continue
                    stack.append((next_row, next_col))
        return res

    res = 0
    for rownum, row in enumerate(graph):
        for colnum, num in enumerate(row):
            if not num:
                res += count_score(rownum, colnum)
    return res

filename = "example.txt"
filename2 = "input.txt"
print(a(filename))
print(a(filename2))