from itertools import islice


START = 'S'
SPLITTER = '^'
EMPTY = '.'

def a(filename: str):
    grid = []
    with open(filename) as file:
        while line := file.readline().rstrip():
            grid.append(line)

    height, width = len(grid), len(grid[0])
    
    first_row = grid[0]
    start_index = first_row.find(START)
    
    DP = [False] * width
    DP[start_index] = True

    res = 0
    for row in islice(grid, 1, height):
        DP_prev = DP
        DP = [False] * width
        for pos, (has_beam, tile) in enumerate(zip(DP_prev, row)):
            if not has_beam:
                continue
            if tile == SPLITTER:
                res += 1
                if pos:
                    DP[pos - 1] = True
                if pos < width - 1:
                    DP[pos + 1] = True
            else:
                DP[pos] = True 
    return res

print(a('./example.txt'))
print(a('./input.txt'))