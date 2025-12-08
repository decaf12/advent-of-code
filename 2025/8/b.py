from itertools import combinations
from math import dist, prod


def b(filename: str, connection_count: int):
    points = []
    with open(filename) as file:
        while line := file.readline().rstrip():
            x, y, z = map(int, line.split(','))
            points.append((x, y, z))
    
    n = len(points)
    sorted_dists = sorted((dist(points[a], points[b]), a, b) for a, b in combinations(range(n), 2))
    
    uf = UnionFind(n)
    for _, a, b in sorted_dists:
        uf.union(a, b)
        if uf.components == 1:
            x1, _, _ = points[a]
            x2, _, _ = points[b]
            return x1 * x2

class UnionFind:
    def __init__(self, n: int):
        self.root_lookup = list(range(n))
        self.rank_lookup = [1] * n
        self.components = n
    
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
        self.components -= 1
        return True

print(b('./example.txt', 10))
print(b('./input.txt', 1000))