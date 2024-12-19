from typing import Dict


class Trie:
    def __init__(self):
        self.next: Dict[str, Trie] = {}
        self.is_end = False
    
    def insert(self, word: str):
        curr = self
        for letter in word:
            curr = curr.next.setdefault(letter, Trie())
        curr.is_end = True

class UnionFind:
    def __init__(self, n: int):
        self.root_lookup = list(range(n))
        self.rank_lookup = [1] * n
    
    def find(self, num: int):
        path = []
        while num != self.root_lookup[num]:
            path.append(num)
            num = self.root_lookup[num]
        for n in path:
            self.root_lookup[n] = num
        return num

    def union(self, num1: int, num2: int):
        root1, root2 = self.find(num1), self.find(num2)
        if root1 == root2:
            return False
        rank1, rank2 = self.rank_lookup[root1], self.rank_lookup[root2]
        if rank1 < rank2:
            root1, root2 = root2, root1
            rank2 = rank1
        self.root_lookup[root2] = root1
        self.rank_lookup[root1] += rank2
        return True