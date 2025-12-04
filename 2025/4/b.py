from collections import deque
from math import inf

ROLL = '@'

def b(filename: str):
    grid = []
    with open(filename) as file:
        while line := file.readline().rstrip():
            grid.append(line)
    
    height, width = len(grid), len(grid[0])
    
    def neighbours(center_row: int, center_col: int):
        for rownum in range(center_row - 1, center_row + 2):
            if rownum not in range(height):
                continue
            for colnum in range(center_col - 1, center_col + 2):
                if colnum not in range(width):
                    continue
                if (rownum, colnum) == (center_row, center_col):
                    continue
                yield rownum, colnum
        
    def count_indegrees(rownum: int, colnum: int):
        return sum(grid[next_row][next_col] == ROLL for next_row, next_col in neighbours(rownum, colnum))
    
    indegree_counter = [[inf for _ in range(width)] for _ in range(height)]
    for rownum, row in enumerate(grid):
        for colnum, tile in enumerate(row):
            if tile == ROLL:
                indegree_counter[rownum][colnum] = count_indegrees(rownum, colnum)
    
    res = 0
    stack = deque((rownum, colnum) for rownum in range(height) for colnum in range(width) if indegree_counter[rownum][colnum] < 4)
    while stack:
        curr_row, curr_col = stack.pop()
        res += 1
        for next_row, next_col in neighbours(curr_row, curr_col):
            if grid[next_row][next_col] != ROLL:
                continue
            indegree_counter[next_row][next_col] -= 1
            if indegree_counter[next_row][next_col] == 3:
                stack.append((next_row, next_col))
    return res

print(b('./example.txt'))
print(b('./input.txt'))