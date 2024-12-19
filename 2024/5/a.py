from typing import List, Set


def a(rules_filename: str, order_filename: str):
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
            if mid_num != -1:
                print(mid_num)
                res += mid_num
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

rules_filename = 'input_rules.txt'
orders_filename = 'input_orders.txt'
print(a(rules_filename, orders_filename))