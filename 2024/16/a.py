from heapq import heappop, heappush
from typing import List


WALL = '#'
START = 'S'
END = 'E'
EMPTY = '.'
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
N = 0
E = 1
S = 2
W = 3
def a(filename: str):
    with open(filename) as file:
        lines = file.read().split('\n')
    graph = [list(row) for row in lines]
    return process(graph)

def process(graph: List[List[str]]):
    height, width = len(graph), len(graph[0])
    visited = [[[False, False, False, False] for _ in range(width)] for _ in range(height)]
    for rownum, row in enumerate(graph):
        for colnum, tile in enumerate(row):
            if tile == START:
                start_row, start_col = rownum, colnum
            elif tile == END:
                end_row, end_col = rownum, colnum
            elif tile == WALL:
                visited[rownum][colnum] = [True, True, True, True]
    pool = [(0, start_row, start_col, E)]
    while pool:
        curr_score, curr_row, curr_col, curr_dir = heappop(pool)
        if (curr_row, curr_col) == (end_row, end_col):
            return curr_score
        if visited[curr_row][curr_col][curr_dir]:
            continue
        visited[curr_row][curr_col][curr_dir] = True

        # straight ahead
        next_dir = curr_dir
        d_row, d_col = directions[next_dir]
        next_row, next_col = curr_row + d_row, curr_col + d_col
        if not visited[next_row][next_col][next_dir]:
            next_score = curr_score + 1
            heappush(pool, (next_score, next_row, next_col, next_dir))
        
        # clockwise
        next_dir = (curr_dir + 1) % 4
        next_row, next_col = curr_row, curr_col
        if not visited[next_row][next_col][next_dir]:
            next_score = curr_score + 1000
            heappush(pool, (next_score, next_row, next_col, next_dir))

        #counterclockwise
        next_dir = (curr_dir - 1) % 4
        next_row, next_col = curr_row, curr_col
        if not visited[next_row][next_col][next_dir]:
            next_score = curr_score + 1000
            heappush(pool, (next_score, next_row, next_col, next_dir))

print(a('example1.txt'))
print(a('example2.txt'))
print(a('input.txt'))