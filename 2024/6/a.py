from lib import Trie, UnionFind


def a(filename: str):
    board = []
    with open(filename) as file:
        while line := file.readline():
            if line[-1] == "\n":
                board.append(line[:-1])
            else:
                board.append(line)
    height, width = len(board), len(board[0])
    BLOCKED = '#'
    GUARD = '^'
    break_early = False
    for rownum, row in enumerate(board):
        for colnum, tile in enumerate(row):
            if tile == GUARD:
                guard_row, guard_col = rownum, colnum
                break_early = True
                break
        if break_early:
            break
    visited = {(guard_row, guard_col)}
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    direction_id = 0
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
            visited.add((guard_row, guard_col))
    return len(visited)

# filename = "example.txt"
filename = "input.txt"

print(a(filename))