from functools import cache
from typing import List, Tuple

def b(filename: str):
    with open(filename) as file:
        patterns = tuple(sorted(file.readline().rstrip().split(", "), key=len))
        file.readline()
        targets = []
        while target := file.readline():
            targets.append(target.rstrip())
    
    @cache
    def DP(target: str, patterns: Tuple[str]):
        if not target:
            return 1
        target_len = len(target)
        res = 0
        for pattern in patterns:
            if len(pattern) > target_len:
                break
            if not target.startswith(pattern):
                continue
            res += DP(target[len(pattern):], patterns)
        return res
    
    return sum(DP(target, patterns) for target in targets)

print(b('example.txt'))
print(b('input.txt'))