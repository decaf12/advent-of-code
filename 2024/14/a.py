from collections import deque
from functools import cache
from math import inf
from typing import List

def a(filename: str, height: int, width: int, steps: int):
    with open(filename) as file:
        lines = file.read().split("\n")

    mid_height = height >> 1
    mid_width = width >> 1
    
    for line in lines:
        (x, y), (dx, dy) = parse(line)
        end_x, end_y = predict(x, y, dx, dy, height, width, steps)
        if end_x in range(mid_height):
            if end_y in range(mid_width):
                NW += 1
            elif end_y in range(mid_width + 1, width):
                NE += 1
        elif end_x in range(mid_height + 1, height):
            if end_y in range(mid_width):
                SW += 1
            elif end_y in range(mid_width + 1, width):
                SE += 1
    print(f"{NW}, {NE}, {SW}, {SE}")
    return NW * NE * SW * SE

def parse(line: str):
    coord, delta = line.split()
    y, x = [int(pos) for pos in coord[2:].split(",")]
    dy, dx = [int(pos) for pos in delta[2:].split(",")]
    return (x, y), (dx, dy)

def predict(x: int, y: int, dx: int, dy: int, height: int, width: int, steps: int):
    end_x = (x + dx * steps) % height
    end_y = (y + dy * steps) % width
    return end_x, end_y
    
filename = "example.txt"
print(a(filename, 7, 11, stap))

# filename2 = "input.txt"
# print(a(filename2, 103, 101))