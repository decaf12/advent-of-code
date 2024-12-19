from collections import deque
from re import findall


def b(filename: str):
    content_arr = []
    res = 0
    valid_patterns = []
    invalid_patterns = []
    with open(filename) as file:
        while line := file.readline():
            content_arr.append(line)
    content = "".join(content_arr)
    n = len(content)
    pos = 0
    enabled = True
    while pos < n:
        if pos < n - 6 and content[pos:pos+7] == "don't()":
            pos += 7
            enabled = False
            continue
        if pos < n - 3 and content[pos:pos+4] == "do()":
            pos += 4
            enabled = True
            continue

        if pos < n - 3 and content[pos:pos+4] == 'mul(':
            pos += 4
            num, is_valid, next_pos = find_num(content, pos)
            if is_valid:
                pos = next_pos
                if pos < n and content[pos] == ",":
                    pos += 1
                    num2, is_valid, next_pos = find_num(content, pos)
                    if is_valid:
                        pos = next_pos
                        if pos < n and content[pos] == ")":
                            pattern = f"mul({num},{num2})"
                            if enabled:
                                valid_patterns.append(pattern)
                                res += num * num2
                            else:
                                invalid_patterns.append(pattern)
                            pos += 1
                            continue
        pos += 1
    return valid_patterns, invalid_patterns, res

def find_num(s: str, sp: int):
    n = len(s)
    if sp >= n:
        return 0, False, n
    if not s[sp].isnumeric() and not s[sp] != '-':
        return 0, False, sp + 1
    num = int(s[sp])
    is_positive = (s[sp] != '-')
    sp += 1
    while sp < n:
        if s[sp].isnumeric():
            num = num * 10 + int(s[sp])
            sp += 1
        else:
            break
    return (num if is_positive else -num), True, sp

def check(filename: str):
    content_arr = []
    with open(filename) as file:
        while line := file.readline():
            content_arr.append(line)
    content = "".join(content_arr)
    regex = r"mul\(-?\d+,-?\d+\)|don't\(\)|do\(\)"
    enabled = True
    valid_patterns = []
    invalid_patterns = []
    res = 0
    for match in findall(regex, content):
        if match == "do()":
            enabled = True
        elif match == "don't()":
            enabled = False
        else:
            if enabled:
                valid_patterns.append(match)
                res += get_product(match)
            else:
                invalid_patterns.append(match)
    return valid_patterns, invalid_patterns, res

def get_product(s: str):
    core = s[4:-1]
    num1, num2 = map(int, core.split(","))
    return num1 * num2

filename = 'input.txt'
method1 = b(filename)
method2 = check(filename)
valid_patterns1, invalid_patterns1, res1 = method1
valid_patterns2, invalid_patterns2, res2 = method2

assert(valid_patterns1 == valid_patterns2)
assert(invalid_patterns1 == invalid_patterns2)
assert(res1 == res2)

print(method1)
print(method2)

print(f"Final result: {res1}")