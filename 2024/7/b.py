from typing import List


def b(filename: str):
    lines = []
    with open(filename) as file:
        while line := file.readline():
            if line[-1] == "\n":
                lines.append(line[:-1])
            else:
                lines.append(line)

    return sum(process(line) for line in lines)

            
def process(line: str):
    target, rest = line.split(":")
    target = int(target)
    nums = [int(num) for num in rest.split()]
    if check(target, nums):
        return target
    return 0

def check(target: int, nums: List[int]):
    n = len(nums)
    total = 0
    def backtracking(pos: int):
        nonlocal total
        if total > target:
            return False
        if pos == n:
            if total == target:
                return True
        else:
            old_total = total
            num = nums[pos]
            total += num
            if backtracking(pos + 1):
                return True
            total_str = f"{old_total}{num}"
            total = int(total_str)
            if backtracking(pos + 1):
                return True
            if pos:
                total = old_total * num
                if backtracking(pos + 1):
                    return True
        return False

    return backtracking(0)

# filename = "example.txt"
filename = "input.txt"
print(b(filename))