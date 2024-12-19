from typing import List
from lib import Trie, UnionFind

BLOCKED = '#'
GUARD = '^'
EMPTY = '.'

def b(filename: str):
    board = []
    with open(filename) as file:
        while line := file.readline():
            if line[-1] == "\n":
                board.append(list(line[:-1]))
            else:
                board.append(list(line))
    break_early = False
    for rownum, row in enumerate(board):
        for colnum, tile in enumerate(row):
            if tile == GUARD:
                guard_row, guard_col = rownum, colnum
                break_early = True
                break
        if break_early:
            break
    res = 0
    for rownum, row in enumerate(board):
        for colnum, tile in enumerate(row):
            if tile == EMPTY:
                board[rownum][colnum] = BLOCKED
                if check(board, guard_row, guard_col):
                    print((rownum, colnum))
                    res += 1
                board[rownum][colnum] = EMPTY
    return res

def check(board: List[List[str]], guard_row: int, guard_col: int):
    height, width = len(board), len(board[0])
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    direction_id = 0
    visited = {(guard_row, guard_col, 0)}
    while True:
        dx, dy = directions[direction_id]
        next_row, next_col = guard_row + dx, guard_col + dy
        if next_row not in range(height) or next_col not in range(width):
            break
        if board[next_row][next_col] == BLOCKED:
            if direction_id == 3:
                direction_id = 0
            else:
                direction_id += 1
        else:
            guard_row, guard_col = next_row, next_col
            if (guard_row, guard_col, direction_id) in visited:
                return True
            visited.add((guard_row, guard_col, direction_id))
    return False

# filename = "example.txt"
filename = "input.txt"

print(b(filename))