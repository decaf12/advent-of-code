from heapq import heappop, heappush
from math import inf
from typing import List


WALL = '#'
START = 'S'
END = 'E'
EMPTY = '.'
SEAT = '0'
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
    lookup = [[[inf, inf, inf, inf] for _ in range(width)] for _ in range(height)]
    for rownum, row in enumerate(graph):
        for colnum, tile in enumerate(row):
            if tile == START:
                start_row, start_col = rownum, colnum
            elif tile == END:
                end_row, end_col = rownum, colnum
    seats = set()
    
    pool = [(0, start_row, start_col, E, [(start_row, start_col)])]
    best_score = inf
    while pool:
        curr_score, curr_row, curr_col, curr_dir, curr_path = heappop(pool)

        if curr_score > lookup[curr_row][curr_col][curr_dir]:
            continue
        lookup[curr_row][curr_col][curr_dir] = curr_score

        if (curr_row, curr_col) == (end_row, end_col):
            if curr_score <= best_score:
                best_score = curr_score
                for seat_row, seat_col in curr_path:
                    seats.add((seat_row, seat_col))
        else:
            # straight ahead
            next_dir = curr_dir
            d_row, d_col = directions[next_dir]
            next_row, next_col = curr_row + d_row, curr_col + d_col
            next_score = curr_score + 1
            next_path = curr_path + [(next_row, next_col)]
            if graph[next_row][next_col] != WALL and next_score <= lookup[next_row][next_col][next_dir]:
                lookup[next_row][next_col][next_dir] = next_score
                heappush(pool, (next_score, next_row, next_col, next_dir, next_path))
            
            # clockwise
            next_dir = (curr_dir + 1) % 4
            next_row, next_col = curr_row, curr_col
            next_score = curr_score + 1000
            next_path = curr_path.copy()
            if next_score <= lookup[next_row][next_col][next_dir]:
                lookup[next_row][next_col][next_dir] = next_score
                heappush(pool, (next_score, next_row, next_col, next_dir, next_path))

            #counterclockwise
            next_dir = (curr_dir - 1) % 4
            next_row, next_col = curr_row, curr_col
            next_score = curr_score + 1000
            next_path = curr_path.copy()
            if next_score <= lookup[next_row][next_col][next_dir]:
                lookup[next_row][next_col][next_dir] = next_score
                heappush(pool, (next_score, next_row, next_col, next_dir, next_path))
    for seat_row, seat_col in seats:
        graph[seat_row][seat_col] = SEAT
    return len(seats)

print(a('example1.txt'))
print(a('example2.txt'))
print(a('input.txt'))