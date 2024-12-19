from collections import deque
from re import findall


def a(filename: str):
    content_arr = []
    res = 0
    valid_count = 0
    with open(filename) as file:
        while line := file.readline():
            content_arr.append(line)
    content = "".join(content_arr)
    n = len(content)
    pos = 0
    while pos < n:
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
                            print(f"mul({num},{num2})")
                            res += num * num2
                            pos += 1
                            valid_count += 1
                            continue
        pos += 1
    return res, valid_count

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
    pattern = r"mul\(-?\d+,-?\d+\)"
    matches = findall(pattern, content)
    return sum(res for res in map(get_product, matches)), len(matches)

def get_product(s: str):
    core = s[4:-1]
    num1, num2 = map(int, core.split(","))
    return num1 * num2

filename = 'input.txt'
print(a(filename))
print(check(filename))