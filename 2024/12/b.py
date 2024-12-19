from collections import defaultdict, deque
from email.policy import default
from itertools import chain
from math import inf
from typing import List

def b(filename: str):
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
        tile = graph[rownum][colnum]
        stack = deque([(rownum, colnum)])
        visited[rownum][colnum] = True
        lookup_by_row = defaultdict(set)
        lookup_by_col = defaultdict(set)
        area = 1
        while stack:
            curr_row, curr_col = stack.pop()
            lookup_by_row[curr_row].add(curr_col)
            lookup_by_col[curr_col].add(curr_row)
            for next_row, next_col in neighbours(curr_row, curr_col):
                if graph[next_row][next_col] != tile:
                    continue
                if visited[next_row][next_col]:
                    continue
                visited[next_row][next_col] = True
                area += 1
                stack.append((next_row, next_col))
        sides = 0
        for rownum, colnums in sorted(lookup_by_row.items()):
            sorted_colnums = sorted(colnums)
            # top_side
            prev_uncovered_colnum = -inf
            for colnum in sorted_colnums:
                if colnum in lookup_by_row[rownum - 1]:
                    continue
                if colnum != prev_uncovered_colnum + 1:
                    sides += 1
                prev_uncovered_colnum = colnum
                
            # bottom side
            prev_uncovered_colnum = -inf
            for colnum in sorted_colnums:
                if colnum in lookup_by_row[rownum + 1]:
                    continue
                if colnum != prev_uncovered_colnum + 1:
                    sides += 1
                prev_uncovered_colnum = colnum
        for colnum, rownums in sorted(lookup_by_col.items()):
            sorted_rownums = sorted(rownums)
            #left side
            prev_uncovered_row = -inf
            for rownum in sorted_rownums:
                if rownum in lookup_by_col[colnum - 1]:
                    continue
                if rownum != prev_uncovered_row + 1:
                    sides += 1
                prev_uncovered_row = rownum
            #right side
            prev_uncovered_row = -inf
            for rownum in sorted_rownums:
                if rownum in lookup_by_col[colnum + 1]:
                    continue
                if rownum != prev_uncovered_row + 1:
                    sides += 1
                prev_uncovered_row = rownum
        return area * sides
   
    res = 0
    for rownum, row in enumerate(visited):
        for colnum, is_visited in enumerate(row):
            if not is_visited:
                res += DFS(rownum, colnum)
    return res

filename = "example.txt"
filename2 = "input.txt"
print(b(filename))
print(b(filename2))