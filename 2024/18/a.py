from heapq import heappop, heappush
from itertools import islice
from typing import List

def a(filename: str, n: int, block_count: int):
    with open(filename) as file:
        blocks = file.read().split("\n")
    blocks = [[int(num) for num in block.split(",")] for block in blocks]
    return process(blocks, n, block_count)

def process(blocks: List[List[int]], n: int, block_count: int):
    visited = [[False for _ in range(n)] for _ in range(n)]
    for rownum, colnum in islice(blocks, 0, block_count):
        visited[rownum][colnum] = True
    pool = [(0, 0, 0)]
    def neighbours(rownum: int, colnum: int):
        if rownum:
            yield rownum - 1, colnum
        if rownum < n - 1:
            yield rownum + 1, colnum
        if colnum:
            yield rownum, colnum - 1
        if colnum < n - 1:
            yield rownum, colnum + 1

    while pool:
        curr_steps, curr_row, curr_col = heappop(pool)
        if (curr_row, curr_col) == (n - 1, n - 1):
            return curr_steps
        if visited[curr_row][curr_col]:
            continue
        visited[curr_row][curr_col] = True
        next_steps = curr_steps + 1
        for next_row, next_col in neighbours(curr_row, curr_col):
            if visited[next_row][next_col]:
                continue
            heappush(pool, (next_steps, next_row, next_col))
    return -1

print(a('example.txt', 7, 12))
print(a('input.txt', 71, 1024))