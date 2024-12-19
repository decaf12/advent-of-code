from typing import List


def a(filename: str):
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
            num = nums[pos]
            total += num
            if backtracking(pos + 1):
                return True
            total -= num
            if pos:
                total *= num
                if backtracking(pos + 1):
                    return True
                total //= num
        return False

    return backtracking(0)

# filename = "example.txt"
filename = "input.txt"
print(a(filename))