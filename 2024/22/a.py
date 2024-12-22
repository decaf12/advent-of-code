from itertools import count
from typing import Counter, Dict, List, Tuple
from collections import Counter, deque
from math import inf

def a(filename: str):
    with open(filename) as file:
        lines = file.read().split("\n")
    nums = [int(num) for num in lines]
    res = 0
    for num in nums:
        end = calc(num, 2000)
        # print(f"{num}: {end}")
        res += end
    return res 

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
    lookup = {start: 0}
    nums = [start]
    num = start
    for round in count(1):
        num = find_next(num)
        if round == rounds:
            return num
        if num in lookup:
            cycle_sp = lookup[num]
            cycle_len = round - cycle_sp
            break
        lookup[num] = round
        nums.append(num)
    rounds_before_cycle = cycle_sp
    remaining_rounds = rounds + 1 - rounds_before_cycle
    remaining_rounds %= cycle_len
    pos_in_round = (remaining_rounds - 1) % cycle_len
    return nums[cycle_sp + pos_in_round]

print(a('example.txt'))
print(a('input.txt'))