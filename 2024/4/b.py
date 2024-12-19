from typing import Dict


def a(filename: str):
    grid = []
    with open(filename) as file:
        while line := file.readline():
            if line[-1] == "\n":
                grid.append(line[:-1])
            else:
                grid.append(line)
    height, width = len(grid), len(grid[0])

    def is_xmas(center_row: int, center_col: int):
        if grid[center_row][center_col] != 'A':
            return False
        NW = grid[center_row - 1][center_col - 1]
        SE = grid[center_row + 1][center_col + 1]
        if sorted((NW, SE)) != ['M', 'S']:
            return False
        NE = grid[center_row - 1][center_col + 1]
        SW = grid[center_row + 1][center_col - 1]
        return sorted((NE, SW)) == ['M', 'S']

    return sum(1 for rownum in range(1, height - 1) for colnum in range(1, width - 1) if is_xmas(rownum, colnum))

# filename = 'example.txt'
filename = 'input.txt'
print(a(filename))