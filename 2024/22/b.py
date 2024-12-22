from itertools import islice, pairwise, product
from typing import Counter, DefaultDict, Dict, List, Tuple
from collections import Counter, defaultdict, deque
from math import inf

def b(filename: str):
    with open(filename) as file:
        lines = file.read().split("\n")
    nums = [int(num) for num in lines]
    paths = [calc(num, 2000) for num in nums]
    path_deltas = [[curr - prev for prev, curr in pairwise(path)] for path in paths]
    lookups = [build_lookup(deltas) for deltas in path_deltas]
    res = 0

    for pos, target_deltas in enumerate(product(range(-9, 10), repeat=4)):
        if not pos % 1000:
            print(pos)
        profit = 0
        for lookup, path, deltas in zip(lookups, paths, path_deltas):
            profit += check(target_deltas, lookup, path, deltas)
        res = max(res, profit)
    return res

P = 113
MOD_PRIME = 10 ** 9 + 7
P_INV = pow(P, MOD_PRIME - 2, MOD_PRIME)
powers = [1] * 4
for pos in range(1, 4):
    powers[pos] = powers[pos - 1] * P % MOD_PRIME

def generate_hash(nums: List[int]):
    curr_hash = 0
    n = len(nums)
    for pos in range(4):
        num = nums[pos]
        power = powers[pos]
        curr_hash = (curr_hash + num * power) % MOD_PRIME
    yield curr_hash
    max_power = powers[-1]
    for pos in range(4, n):
        num = nums[pos]
        reject = nums[pos - 4]
        curr_hash = ((curr_hash - reject) * P_INV + num * max_power) % MOD_PRIME
        yield curr_hash

def build_lookup(nums: List[int]):
    lookup = defaultdict(list)
    for sp, hash in enumerate(generate_hash(nums)):
        lookup[hash].append(sp)
    return lookup

def check(target_deltas: Tuple[int], lookup: DefaultDict[int, List[int]], path: List[int], deltas: List[int]):
    [target_hash] = list(generate_hash(target_deltas))
    if target_hash not in lookup:
        return 0
    for sp in lookup[target_hash]:
        if all(a == b for a, b in zip(target_deltas, islice(deltas, sp, sp + 4))):
            return path[sp + 4]
    return 0

memo = {}

MOD = 16777216
def find_next(num: int):
    if num in memo:
        return memo[num]
    start_num = num
    res = num
    res <<= 6
    res ^= num
    res %= MOD

    num = res
    res >>= 5
    res ^= num
    res %= MOD

    num = res
    res <<= 11
    res ^= num
    res %= MOD
    memo[start_num] = res
    return res

def calc(start: int, rounds: int):
    nums = [start % 10]
    num = start
    for _ in range(rounds):
        num = find_next(num)
        nums.append(num % 10)
    return nums

print(b('example_b.txt'))
print(b('input.txt'))