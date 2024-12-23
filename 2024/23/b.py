from copy import deepcopy
from itertools import islice
from typing import Counter, Dict, List, Tuple
from collections import Counter, defaultdict, deque
from math import inf

def b(filename: str):
    with open(filename) as file:
        lines = file.read().split("\n")

    graph = defaultdict(set)
    for line in lines:
        machine_a, machine_b = line.split("-")
        graph[machine_a].add(machine_b)
        graph[machine_b].add(machine_a)
    groups = {(node,) for node in graph}
    print(f"size of graph: {len(graph)}")
    for node_id, node in enumerate(graph):
        if not node_id % 20:
            print(f'node {node_id}')
        next_groups = deepcopy(groups)
        for group in groups:
            if all(node in graph[member] for member in group):
                new_group = tuple(sorted(group) + [node])
                next_groups.add(new_group)
        groups = next_groups
    max_group = max(groups, key=len)
    return ",".join(sorted(max_group))

print(b('example.txt'))
print(b('input.txt'))