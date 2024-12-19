from collections import deque
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
    return process(lines)

def process(graph: List[str]):
    height, width = len(graph), len(graph[0])
    visited = [[False for _ in range(width)] for _ in range(height)]
    def neighbours(rownum: int, colnum: int):
        if rownum:
            yield rownum - 1, colnum
        if rownum < height - 1:
            yield rownum + 1, colnum
        if colnum:
            yield rownum, colnum - 1
        if colnum < width - 1:
            yield rownum, colnum + 1

    def DFS(rownum: int, colnum: int):
        area = 1
        perimeter = 4
        tile = graph[rownum][colnum]
        stack = deque([(rownum, colnum)])
        visited[rownum][colnum] = True
        while stack:
            curr_row, curr_col = stack.pop()
            for next_row, next_col in neighbours(curr_row, curr_col):
                if graph[next_row][next_col] != tile:
                    continue
                perimeter -= 1
                if visited[next_row][next_col]:
                    continue
                visited[next_row][next_col] = True
                area += 1
                perimeter += 4
                stack.append((next_row, next_col))
        return area * perimeter
    
    res = 0
    for rownum, row in enumerate(visited):
        for colnum, is_visited in enumerate(row):
            if not is_visited:
                res += DFS(rownum, colnum)
    return res

filename = "example.txt"
filename2 = "input.txt"
print(a(filename))
print(a(filename2))