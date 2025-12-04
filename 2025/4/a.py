ROLL = '@'

def a(filename: str):
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
    
    def is_valid(rownum: int, colnum: int):
        if grid[rownum][colnum] != ROLL:
            return False
        return sum(grid[next_row][next_col] == ROLL for next_row, next_col in neighbours(rownum, colnum)) < 4
    return sum(is_valid(rownum, colnum) for rownum in range(height) for colnum in range(width))

print(a('./example.txt'))
print(a('./input.txt'))