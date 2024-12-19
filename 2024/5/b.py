from collections import deque
from typing import List, Set


def b(rules_filename: str, order_filename: str):
    follower_lookup = [set() for _ in range(100)]
    with open(rules_filename) as file:
        while line := file.readline():
            first, second = map(int, line.split("|"))
            follower_lookup[first].add(second)
    res = 0
    with open(order_filename) as file:
        while line := file.readline():
            nums = [int(num) for num in line.split(",")]
            mid_num = check(nums, follower_lookup)
            if mid_num == -1:
                new_midnum = topo_sort(nums, follower_lookup)
                print(new_midnum)
                res += new_midnum
    return res

def check(nums: List[int], follower_lookup: List[Set[int]]):
    n = len(nums)
    if n == 1:
        return nums[0]
    encountered = set()
    for num in nums:
        if encountered & follower_lookup[num]:
            return -1
        encountered.add(num)
    return nums[n >> 1]

def topo_sort(nums: List[int], follower_lookup: List[Set[int]]):
    num_set = set(nums)
    topo = []
    UNPROCESSED = 0
    PROCESSING = 1
    FINISHED = 2
    colour_lookup = [UNPROCESSED] * 100
    def DFS(num: int):
        colour_lookup[num] = PROCESSING
        for next_num in follower_lookup[num]:
            if next_num not in num_set:
                continue
            if colour_lookup[next_num] == UNPROCESSED:
                DFS(next_num)
        colour_lookup[num] = FINISHED
        topo.append(num)
    
    for num in nums:
        if colour_lookup[num] == UNPROCESSED:
            DFS(num)
    n = len(topo)
    return topo[n >> 1]    

rules_filename = 'input_rules.txt'
orders_filename = 'input_orders.txt'
print(b(rules_filename, orders_filename))