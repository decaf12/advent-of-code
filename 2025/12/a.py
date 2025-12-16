from io import TextIOWrapper
from itertools import chain
from typing import List
OCCUPIED = '#'
EMPTY = '.'

TRIVIALLY_PASS = 1
TRIVIALLY_FAIL = -1
UNCLEAR = 0

def a(filename: str):
    presents = []
    trivially_pass_count = 0
    trivially_fail_count = 0
    unclear_count = 0
    with open(filename) as file:
        for _ in range(6):
            presents.append(read_present(file))
        occupied_lookup = [count_occupied(present) for present in presents]
        while line := file.readline().rstrip():
            height, width, requirements = parse_grid(line)
            verdict = calc(height, width, requirements, occupied_lookup)
            if verdict == TRIVIALLY_PASS:
                trivially_pass_count += 1
            elif verdict == TRIVIALLY_FAIL:
                trivially_fail_count += 1
            else:
                unclear_count += 1
    print(f"trivially pass: {trivially_pass_count}, trivially fail: {trivially_fail_count}, unclear: {unclear_count}")

def count_occupied(present: List[str]):
    return sum(tile == OCCUPIED for tile in chain.from_iterable(present))

def read_present(file: TextIOWrapper):
    file.readline()
    present = []
    for _ in range(3):
        present.append(file.readline().rstrip())
    file.readline()
    return present

def parse_grid(line: str):
    size, requirements_str = line.split(": ")
    width, height = map(int, size.split('x'))
    requirements = [int(req) for req in requirements_str.split()]
    return height, width, requirements

def calc(height: int, width: int, requirements: List[int], occupied_lookup: List[int]):
    total_requirement = sum(requirements)
    if (height // 3) * (width // 3) >= total_requirement:
        return TRIVIALLY_PASS
    total_area = sum(quantity * area for quantity, area in zip(requirements, occupied_lookup))
    if height * width < total_area:
        return TRIVIALLY_FAIL
    return UNCLEAR

print(a('./example.txt'))
print(a('./input.txt'))