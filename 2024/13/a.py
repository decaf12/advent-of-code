from collections import deque
from functools import cache
from math import inf
from typing import List

def a(filename: str):
    res = 0
    with open(filename) as file:
        while True:
            button_a = file.readline()
            # print(button_a)
            if not button_a:
                break
            button_b = file.readline()
            prize = file.readline()
            file.readline()
            x1, y1 = parse(button_a, "+")
            x2, y2 = parse(button_b, "+")
            x_prize, y_prize = parse(prize, "=")

            @cache
            def DP(curr_x: int, curr_y: int, a_pressed: int = 0, b_pressed: int = 0):
                if curr_x == x_prize and curr_y == y_prize:
                    return 0
                if curr_x > x_prize or curr_y > y_prize:
                    return inf
                if a_pressed > 100 or b_pressed > 100:
                    return inf
                next_x1, next_y1 = curr_x + x1, curr_y + y1
                next_x2, next_y2 = curr_x + x2, curr_y + y2
                return min(3 + DP(next_x1, next_y1, a_pressed + 1, b_pressed), 1 + DP(next_x2, next_y2, a_pressed, b_pressed + 1))

            coins = DP(0, 0)
            # print(coins)
            if coins != inf:
                res += coins
    return res

def parse(line: str, separator: str):
    left, right = line.split(", ")
    prefix_sp_x = left.find(f"X{separator}")
    x_str = left[prefix_sp_x + 2:]
    y_str = right[2:]
    return int(x_str), int(y_str)

filename = "example.txt"
filename2 = "input.txt"
print(a(filename))
print(a(filename2))