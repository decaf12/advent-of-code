from collections import deque
from itertools import count
from math import inf
from typing import List

def b(filename: str, height: int, width: int):
    with open(filename) as file:
        lines = file.read().split("\n")
    repeats = 0
    grid = [[0 for _ in range(width)] for _ in range(height)]
    robots = []
    for line in lines:
        (x, y), (dx, dy) = parse(line)
        grid[x][y] += 1
        if grid[x][y] == 2:
             repeats += 1
        robots.append((x, y, dx, dy))
    for step in count(1):
        next_robots = []
        for x, y, dx, dy in robots:
            grid[x][y] -= 1
            if grid[x][y] == 1:
                repeats -= 1
            next_x, next_y = predict(x, y, dx, dy, height, width, 1)
            grid[next_x][next_y] += 1
            if grid[next_x][next_y] == 2:
                repeats += 1
            next_robots.append((next_x, next_y, dx, dy))
        if not repeats:
            return step
        robots = next_robots

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
print(b(filename, 7, 11))

filename2 = "input.txt"
print(b(filename2, 103, 101))