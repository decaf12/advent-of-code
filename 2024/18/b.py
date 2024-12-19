from typing import List

def b(filename: str, n: int):
    with open(filename) as file:
        blocks = file.read().split("\n")
    blocks = [[int(num) for num in reversed(block.split(","))] for block in blocks]
    return process(blocks, n)

def process(blocks: List[List[int]], n: int):
    EMPTY = "."
    BLOCKED = '#'
    grid = [[EMPTY for _ in range(n)] for _ in range(n)]
    for rownum, colnum in blocks:
        grid[rownum][colnum] = BLOCKED

    def neighbours(rownum: int, colnum: int):
        if rownum:
            yield rownum - 1, colnum
        if rownum < n - 1:
            yield rownum + 1, colnum
        if colnum:
            yield rownum, colnum - 1
        if colnum < n - 1:
            yield rownum, colnum + 1
        
    def empty_neighbours(rownum: int, colnum: int):
        for next_row, next_col in neighbours(rownum, colnum):
            if grid[next_row][next_col] == EMPTY:
                yield next_row, next_col

    uf = UnionFind(n)
    for rownum, row in enumerate(grid):
        for colnum, tile in enumerate(row):
            if tile == EMPTY:
                for next_row, next_col in empty_neighbours(rownum, colnum):
                    uf.union(rownum, colnum, next_row, next_col)
    
    for block_row, block_col in reversed(blocks):
        grid[block_row][block_col] = EMPTY
        for next_row, next_col in empty_neighbours(block_row, block_col):
            uf.union(block_row, block_col, next_row, next_col)
        if uf.find(0, 0) == uf.find(n - 1, n - 1):
            return block_col, block_row

class UnionFind:
    def __init__(self, n: int):
        self.root_lookup = [[(rownum, colnum) for colnum in range(n)] for rownum in range(n)]
        self.rank_lookup = [[1 for _ in range(n)] for _ in range(n)]
    
    def find(self, rownum: int, colnum: int):
        path = []
        while (rownum, colnum) != self.root_lookup[rownum][colnum]:
            path.append((rownum, colnum))
            rownum, colnum = self.root_lookup[rownum][colnum]
        for row, col in path:
            self.root_lookup[row][col] = (rownum, colnum)
        return rownum, colnum

    def union(self, row1: int, col1: int, row2: int, col2: int):
        root_r1, root_c1 = self.find(row1, col1)
        root_r2, root_c2 = self.find(row2, col2)
        if (root_r1, root_c1) == (root_r2, root_c2):
            return False
        rank1 = self.rank_lookup[root_r1][root_c1]
        rank2 = self.rank_lookup[root_r2][root_c2]
        if rank1 < rank2:
            (root_r1, root_c1), (root_r2, root_c2) = (root_r2, root_c2), (root_r1, root_c1)
            rank2 = rank1
        self.root_lookup[root_r2][root_c2] = (root_r1, root_c1)
        self.rank_lookup[root_r1][root_c1] += rank2
        return True

print(b('example.txt', 7))
print(b('input.txt', 71))