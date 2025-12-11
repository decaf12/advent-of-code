from itertools import chain, combinations, pairwise
from typing import List, Tuple

UP = 'UP'
LEFT = 'LEFT'
DOWN = 'DOWN'
RIGHT = 'RIGHT'

def b(filename: str):
    coords = []
    with open(filename) as file:
        while line := file.readline().rstrip():
            colnum, rownum = map(int, line.split(','))
            coords.append((rownum, colnum))

    tour = build_tour(coords)
    n = len(coords)
    res = 0
    for sp, ep in combinations(range(n), 2):
        if check(coords, tour, sp, ep):
            start_row, start_col = coords[sp]
            end_row, end_col = coords[ep]

            N, S = sorted((start_row, end_row))
            W, E = sorted((start_col, end_col))
            res = max(res, (S - N + 1) * (E - W + 1))
    return res

def build_tour(coords: List[Tuple[int]]):
    n = len(coords)
    route = chain(range(n), (0, ))
    res = []
    for from_id, to_id in pairwise(route):
        from_row, from_col = coords[from_id]
        to_row, to_col = coords[to_id]
        if from_row == to_row:
            dir = RIGHT if to_col > from_col else LEFT
            res.append((dir, from_col, to_col, from_row))
        else:
            dir = DOWN if to_row > from_row else UP
            res.append((dir, from_row, to_row, from_col))
    return res
        
def check(coords: List[Tuple[int]], tour: List[Tuple[int]], sp: int, ep: int):
    start_row, start_col = coords[sp]
    end_row, end_col = coords[ep]

    N, S = sorted((start_row, end_row))
    W, E = sorted((start_col, end_col))

    has_horizontal_top = False
    has_horizontal_bottom = False
    has_vertical_left = False
    has_vertical_right = False

    for dir, *rest in tour:
        if dir == UP:
            from_row, to_row, col = rest
            if col <= W:
                has_vertical_left = True
            if col >= E:
                has_vertical_right = True
            if from_row >= S and to_row < S:
                if col in range(W + 1, E):
                    return False
        elif dir == DOWN:
            from_row, to_row, col = rest
            if col <= W:
                has_vertical_left = True
            if col >= E:
                has_vertical_right = True
            if from_row <= N and to_row > N:
                if col in range(W + 1, E):
                    return False
        elif dir == LEFT:
            from_col, to_col, row = rest
            if row <= N:
                has_horizontal_top = True
            if row >= S:
                has_horizontal_bottom = True
            if from_col >= E and to_col < E:
                if row in range(N + 1, S):
                    return False
        elif dir == RIGHT:
            from_col, to_col, row = rest
            if row <= N:
                has_horizontal_top = True
            if row >= S:
                has_horizontal_bottom = True
            if from_col <= W and to_col > W:
                if row in range(N + 1, S):
                    return False
    return has_horizontal_top and has_horizontal_bottom and has_vertical_left and has_vertical_right

print(b('./example.txt'))
print(b('./input.txt'))