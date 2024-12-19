from collections import deque
from functools import cache
from itertools import count
from math import inf
from typing import List

def b(filename: str):
    res = 0
    game_id = 0
    with open(filename) as file:
        while True:
            game_id += 1
            button_a = file.readline()
            # print(button_a)
            if not button_a:
                break
            button_b = file.readline()
            prize = file.readline()
            file.readline()
            x1, y1 = parse(button_a, "+")
            x2, y2 = parse(button_b, "+")
            c, d = parse(prize, "=")
            c += 10000000000000
            d += 10000000000000

            if x1 * y2 != y1 * x2:
                b, remainder = divmod(c * y1 - d * x1, x2 * y1 - x1 * y2)
                if remainder:
                    continue
                a, remainder = divmod(c - b * x2, x1)
                if remainder:
                    continue
                if a < 0 or b < 0:
                    continue
                res += 3 * a + b
            else:
                coins = inf
                for b in count():
                    a, remainder = divmod(c - y1 * b, x1)
                    if a < 0:
                        break
                    if remainder:
                        continue
                    coins = min(coins, 3 * a + b)
                if coins != inf:
                    res += coins
                (f"game {game_id}: {res}")
    return res

def parse(line: str, separator: str):
    left, right = line.split(", ")
    prefix_sp_x = left.find(f"X{separator}")
    x_str = left[prefix_sp_x + 2:]
    y_str = right[2:]
    return int(x_str), int(y_str)

filename = "example.txt"
print(b(filename))

filename2 = "input.txt"
print(b(filename2))