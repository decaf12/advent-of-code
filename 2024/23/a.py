from itertools import combinations
from typing import Counter, Dict, List, Tuple
from collections import Counter, defaultdict, deque
from math import comb, inf

def a(filename: str):
    with open(filename) as file:
        lines = file.read().split("\n")

    graph = defaultdict(set)
    for line in lines:
        machine_a, machine_b = line.split("-")
        graph[machine_a].add(machine_b)
        graph[machine_b].add(machine_a)
    one_t = two_t = three_t = 0
    for node, neighbours in graph.items():
        if node[0] != 't':
            continue
        for node1, node2 in combinations(neighbours, 2):
            if node1 not in graph[node2]:
                continue
            if node1[0] == 't' and node2[0] == 't':
                three_t += 1
            elif node1[0] == 't' or node2[0] == 't':
                two_t += 1
            else:
                one_t += 1
    return one_t + (two_t >> 1) + three_t // 3

print(a('example.txt'))
print(a('input.txt'))