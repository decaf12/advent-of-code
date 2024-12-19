from functools import cache
from typing import List, Tuple

def a(filename: str):
    with open(filename) as file:
        patterns = tuple(sorted(file.readline().rstrip().split(", "), key=len))
        file.readline()
        targets = []
        while target := file.readline():
            targets.append(target.rstrip())
    
    @cache
    def DP(target: str, patterns: Tuple[str]):
        if not target:
            return True
        target_len = len(target)
        for pattern in patterns:
            if len(pattern) > target_len:
                break
            if not target.startswith(pattern):
                continue
            if DP(target[len(pattern):], patterns):
                return True
        return False
    
    return sum(DP(target, patterns) for target in targets)

print(a('example.txt'))
print(a('input.txt'))