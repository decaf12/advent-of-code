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
    def neighbours(rownum: int, colnum: int):
        for row in range(rownum - 1, rownum + 2):
            if row not in range(height):
                continue
            for col in range(colnum - 1, colnum + 2):
                if col not in range(width):
                    continue
                if (row, col) != (rownum, colnum):
                    yield row, col
    
    trie = Trie()
    trie.insert('XMAS')
    res = 0
    def DFS(rownum: int, colnum: int, node: Trie, dx: int = 0, dy: int = 0):
        nonlocal res
        if node.is_end:
            res += 1
            return
        if not dx and not dy:
            next_coords = neighbours(rownum, colnum)
        else:
            next_coords = [(rownum + dx, colnum + dy)]

        for next_row, next_col in next_coords:
            if next_row not in range(height) or next_col not in range(width):
                continue
            next_letter = grid[next_row][next_col]
            if next_letter not in node.next:
                continue
            DFS(next_row, next_col, node.next[next_letter], next_row - rownum, next_col - colnum)

    for rownum, row in enumerate(grid):
        for colnum, letter in enumerate(row):
            if letter == "X":
                DFS(rownum, colnum, trie.next['X'])
    return res

class Trie:
    def __init__(self):
        self.next: Dict[str, Trie] = {}
        self.is_end = False
    
    def insert(self, word: str):
        curr = self
        for letter in word:
            curr = curr.next.setdefault(letter, Trie())
        curr.is_end = True

# filename = 'example.txt'
filename = 'input.txt'
print(a(filename))