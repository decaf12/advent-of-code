from itertools import islice


START = 'S'
SPLITTER = '^'
EMPTY = '.'

def b(filename: str):
    grid = []
    with open(filename) as file:
        while line := file.readline().rstrip():
            grid.append(line)

    height, width = len(grid), len(grid[0])
    
    first_row = grid[0]
    start_index = first_row.find(START)
    
    DP = [0] * width
    DP[start_index] = 1

    for row in islice(grid, 1, height):
        DP_prev = DP
        DP = [0] * width
        for pos, (path_count, tile) in enumerate(zip(DP_prev, row)):
            if not path_count:
                continue
            if tile == SPLITTER:
                if pos:
                    DP[pos - 1] += path_count
                if pos < width - 1:
                    DP[pos + 1] += path_count
            else:
                DP[pos] += path_count
    return sum(DP)

print(b('./example.txt'))
print(b('./input.txt'))