from functools import cache
from itertools import product
from typing import Counter, Dict, List, Tuple
from collections import Counter, deque
from math import inf

def a(filename: str):
    with open(filename) as file:
        instructions = file.read().split("\n")
    res = 0
    for instruction in instructions:
        numeric_val = parse_numeric(instruction)
        length = DP_numeric(instruction)
        # print(f"{length}, {numeric_val}")
        res += length * numeric_val
    return res

def parse_numeric(instruction: str):
    return int(instruction[:-1])

ACTION = 'A'
FORBIDDEN = '#'
numeric_keypad = [
    ['7', '8', '9'],
    ['4', '5', '6'],
    ['1', '2', '3'],
    [FORBIDDEN, '0', ACTION]
]

N = '^'
S = 'v'
W = '<'
E = '>'
directional_keypad = [
    [FORBIDDEN, N, ACTION],
    [W, S, E]
]

def calc_directions(instruction1: str, instruction2: str, keypad: List[List[str]], keypad_lookup: Dict[str, Tuple[int, int]]):
    row1, col1 = keypad_lookup[instruction1]
    row2, col2 = keypad_lookup[instruction2]
    abs_d_row = abs(row1 - row2)
    abs_d_col = abs(col1 - col2)
    can_move_vertically_first = (keypad[row2][col1] != FORBIDDEN)
    can_move_horizontally_first = (keypad[row1][col2] != FORBIDDEN)
    directions = []
    if col2 == col1:
        # N
        if row2 < row1:
            directions = [N * abs_d_row]
        # S
        elif row2 > row1:
            directions = [S * abs_d_row]
        # None
        else:
            directions = ['']
    elif col2 > col1:
        # NE
        if row2 < row1:
            if can_move_vertically_first:
                directions.append(N * abs_d_row + E * abs_d_col)
            if can_move_horizontally_first:
                directions.append(E * abs_d_col + N * abs_d_row)
        # SE
        elif row2 > row1:
            if can_move_vertically_first:
                directions.append(S * abs_d_row + E * abs_d_col)
            if can_move_horizontally_first:
                directions.append(E * abs_d_col + S * abs_d_row)
        # E
        else:
            directions = [E * abs_d_col]
    else:
        # NW
        if row2 < row1:
            if can_move_vertically_first:
                directions.append(N * abs_d_row + W * abs_d_col)
            if can_move_horizontally_first:
                directions.append(W * abs_d_col + N * abs_d_row)
        # SW
        elif row2 > row1:
            if can_move_vertically_first:
                directions.append(S * abs_d_row + W * abs_d_col)
            if can_move_horizontally_first:
                directions.append(W * abs_d_col + S * abs_d_row)
        # W
        else:
            directions = [W * abs_d_col]
    return [f"{direction}{ACTION}" for direction in directions]

numeric_keypad_lookup = {numeric_keypad[rownum][colnum]: (rownum, colnum) for rownum in range(4) for colnum in range(3)}
directional_keypad_lookup = {directional_keypad[rownum][colnum]: (rownum, colnum) for rownum in range(2) for colnum in range(3)}

numeric_directions_lookup = {(instruction1, instruction2): calc_directions(instruction1, instruction2, numeric_keypad, numeric_keypad_lookup) for instruction1, instruction2 in product('0123456789A', repeat=2)}
directional_directions_lookup = {(instruction1, instruction2): calc_directions(instruction1, instruction2, directional_keypad, directional_keypad_lookup) for instruction1, instruction2 in product('^v<>A', repeat=2)}


@cache
def DP_numeric(instructions: str):
    prev_instruction = ACTION

    res = 0
    next_indirections = 2
    next_instructions = []
    for instruction in instructions:
        directions = numeric_directions_lookup[(prev_instruction, instruction)]
        min_instruction_len = inf
        shortest_instruction = ""
        for direction in directions:
            instruction_len = DP_directional(direction, next_indirections)
            if instruction_len < min_instruction_len:
                min_instruction_len = instruction_len
                shortest_instruction = direction
                next_instructions.append(shortest_instruction)
        res += min_instruction_len
        prev_instruction = instruction
    return res

@cache
def DP_directional(instructions: str, indirections: int):
    prev_instruction = ACTION
    if not indirections:
        return len(instructions)

    res = 0
    next_indirections = indirections - 1
    next_instructions = []
    for  instruction in instructions:
        directions = directional_directions_lookup[(prev_instruction, instruction)]
        min_instruction_len = inf
        shortest_instruction = ""
        for direction in directions:
            instruction_len = DP_directional(direction, next_indirections)
            if instruction_len < min_instruction_len:
                min_instruction_len = instruction_len
                shortest_instruction = direction
        next_instructions.append(shortest_instruction)
        res += min_instruction_len
        prev_instruction = instruction
    return res


print(a('example.txt'))
print(a('input.txt'))