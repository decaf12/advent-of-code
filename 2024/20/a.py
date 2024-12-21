from typing import Counter, List, Tuple
from collections import Counter, defaultdict, deque
from math import inf

BLOCKED = '#'
START = 'S'
END = 'E'

S = -1
N = 1
NE = 2
SW = -2
E = 3
W = -3
SE = 4
NW = -4

def a(filename: str):
    with open(filename) as file:
        graph = file.read().split("\n")

    for rownum, row in enumerate(graph):
        for colnum, tile in enumerate(row):
            if tile == START:
                start_row, start_col = rownum, colnum
            elif tile == END:
                end_row, end_col = rownum, colnum
    
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
    
    lookup = [[inf for _ in range(width)] for _ in range(height)]
    lookup[end_row][end_col] = 0
    queue = deque([(end_row, end_col)])
    while queue:
        curr_row, curr_col = queue.popleft()
        curr_dist = lookup[curr_row][curr_col]
        next_dist = curr_dist + 1
        for next_row, next_col in neighbours(curr_row, curr_col):
            if graph[next_row][next_col] == BLOCKED:
                continue
            if lookup[next_row][next_col] != inf:
                continue
            lookup[next_row][next_col] = next_dist
            queue.append((next_row, next_col))

    def pairs():
        for rownum in range(1, height - 1):
            for colnum in range(1, width - 1):
                if graph[rownum][colnum] == BLOCKED:
                    continue
                for abs_d_col in range(21):
                    max_abs_d_row = 20 - abs_d_col
                    for d_col in (-abs_d_col, abs_d_col):
                        for abs_d_row in range(max_abs_d_row + 1):
                            for d_row in (abs_d_row, -abs_d_row):
                                if not d_col and not d_row:
                                    continue
                                next_row, next_col = rownum + d_row, colnum + d_col
                                if next_row not in range(height) or next_col not in range(width):
                                    continue
                                if graph[next_row][next_col] == BLOCKED:
                                    continue
                                yield (rownum, colnum), (next_row, next_col)

    shortcuts_lookup = defaultdict(set)
    for (entry_row, entry_col), (exit_row, exit_col) in pairs():
        if (entry_row, entry_col, exit_row, exit_col) == (start_row, start_col, end_row, end_col - 2):
            print('test')
        dist_to_entry = lookup[entry_row][entry_col]
        dist_to_exit = lookup[exit_row][exit_col]
        manhattan_dist = abs(exit_row - entry_row) + abs(exit_col - entry_col)
        new_dist_to_entry = dist_to_exit + manhattan_dist
        time_saved = dist_to_entry - new_dist_to_entry
        if time_saved > 0:
            shortcuts_lookup[time_saved].add((entry_row, entry_col, exit_row, exit_col))
    tacos = sorted((time_saved, len(members)) for time_saved, members in shortcuts_lookup.items() if time_saved >= 50)
    return sum(len(members) for time_saved, members in shortcuts_lookup.items() if time_saved >= 100)
                

print(a('example.txt'))
print(a('input.txt'))