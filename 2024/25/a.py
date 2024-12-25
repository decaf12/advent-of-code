from typing import Counter, Dict, List, Tuple
from collections import Counter, defaultdict, deque
from math import inf

def a(filename: str, rowcount: int):
    keys = set()
    locks = set()
    trie = Trie(rowcount)
    with open(filename) as file:
        while True:
            top_row = file.readline().rstrip()
            is_lock = all(tile == '#' for tile in top_row)
            height_graph = []
            for _ in range(6):
                height_graph.append(file.readline().rstrip())
            if not is_lock:
                height_graph = [top_row] + height_graph[:-1]
            width = len(height_graph[0])
            heights = [0] * width
            for row in height_graph:
                for colnum, tile in enumerate(row):
                    if tile == '#':
                        heights[colnum] += 1
            if is_lock:
                trie.insert(heights)
                locks.add(tuple(heights))
            else:
                keys.add(tuple(heights))
            if not file.readline():
                break
    return sum(trie.count_matches(key) for key in keys)

class Trie:
    def __init__(self, total: int = 0):
        self.next: Dict[int, Trie] = {}
        self.is_end = False
        self.total = total
    
    def insert(self, nums: List[int]):
        curr = self
        for digit in nums:
            curr = curr.next.setdefault(digit, Trie())
        curr.is_end = True
    
    def count_matches(self, nums: List[int]):
        curr = self
        stack = deque([(curr, 0)])
        res = 0
        while stack:
            curr_parent, curr_pos = stack.pop()
            if curr_parent.is_end:
                res += 1
                continue
            curr_digit = nums[curr_pos]
            next_pos = curr_pos + 1
            max_match_digit = self.total - curr_digit
            for digit, child in sorted(curr_parent.next.items()):
                if digit > max_match_digit:
                    break
                stack.append((child, next_pos))
        return res
                

print(a('example.txt', 5))
print(a('input.txt', 5))