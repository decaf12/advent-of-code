from collections import defaultdict
from itertools import combinations


def a(filename: str):
    lookup = defaultdict(list)
    with open(filename) as file:
        while line := file.readline().rstrip():
            x, y = map(int, line.split(','))
            lookup[x].append(y)
    
    for members in lookup.values():
        members.sort()
    
    res = 0
    for x1, x2 in combinations(lookup, 2):
        height = abs(x1 - x2) + 1
        ys_1 = lookup[x1]
        ys_2 = lookup[x2]
        min_y1, max_y1 = min(ys_1), max(ys_1)
        min_y2, max_y2 = min(ys_2), max(ys_2)
        max_width = max(abs(max_y1 - min_y2), abs(max_y2 - min_y1)) + 1
        res = max(res, height * max_width)
    return res

print(a('./example.txt'))
print(a('./input.txt'))