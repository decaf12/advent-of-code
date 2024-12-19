from collections import defaultdict
from itertools import combinations
from math import gcd


def a(filename: str):
    lines = []
    with open(filename) as file:
        while line := file.readline():
            if line[-1] == "\n":
                lines.append(line[:-1])
            else:
                lines.append(line)

    location_lookup = defaultdict(list)
    for rownum, row in enumerate(lines):
        for colnum, tile in enumerate(row):
            if tile != ".":
                location_lookup[tile].append((rownum, colnum))

    height, width = len(lines), len(lines[0])
    antinodes = set()
    for locations in location_lookup.values():
        locations.sort()
        for (row1, col1), (row2, col2) in combinations(locations, 2):
            antinodes.add((row1, col1))
            antinodes.add((row2, col2))
            d_row, d_col = row2 - row1, col2 - col1
            curr_row, curr_col = row2, col2
            while True:
                curr_row += d_row
                curr_col += d_col
                if curr_row in range(height) and curr_col in range(width):
                    antinodes.add((curr_row, curr_col))
                else:
                    break
            curr_row, curr_col = row1, col1
            while True:
                curr_row -= d_row
                curr_col -= d_col
                if curr_row in range(height) and curr_col in range(width):
                    antinodes.add((curr_row, curr_col))
                else:
                    break
    return len(antinodes)
                

filename = "example.txt"
filename2 = "input.txt"
print(a(filename))
print(a(filename2))