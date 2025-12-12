from collections import defaultdict, deque
from math import inf
from typing import List


def a(filename: str):
    res = 0
    with open(filename) as file:
        while line := file.readline().rstrip():
            target_mask, switch_masks = parse(line)
            subtotal = calc(target_mask, switch_masks)
            res += subtotal
    return res

def calc(target: int, nums: List[int]):
    if not target:
        return 0

    lookup = defaultdict(lambda: inf)
    lookup[0] = 0
    for num in nums:
        for prev_num, prev_steps in list(lookup.items()):
            next_num = num ^ prev_num
            next_steps = prev_steps + 1
            lookup[next_num] = min(lookup[next_num], next_steps)
    return lookup[target]

def parse(line: str):
    end_square_bracket_pos = line.find(']')
    target_lights = line[1:end_square_bracket_pos]
    target_mask = build_target_mask(target_lights)

    first_brace_pos = line.find('{')

    middle = line[end_square_bracket_pos + 1: first_brace_pos - 1]
    switches = middle.split()
    switch_masks = [build_switch_mask(switch) for switch in switches]
    return target_mask, switch_masks

def build_target_mask(target: str):
    mask = 0
    for pos, light in enumerate(target):
        if light == '#':
            mask |= 1 << pos
    return mask

def build_switch_mask(switch: str):
    switch = switch[1: -1]
    lights = map(int, switch.split(','))
    mask = 0
    for light in lights:
        mask |= 1 << light
    return mask

print(a('./example.txt'))
print(a('./input.txt'))