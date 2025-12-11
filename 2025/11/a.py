from collections import defaultdict, deque
from typing import Counter


def a(filename: str):
    graph = defaultdict(list)
    indegree_lookup = Counter()
    all_nodes = set()
    with open(filename) as file:
        while line := file.readline().rstrip():
            source, destinations = line.split(": ")
            all_nodes.add(source)
            destination_list = destinations.split()
            graph[source] = destination_list
            for destination in destination_list:
                indegree_lookup[destination] += 1
                all_nodes.add(destination)
    
    counter = Counter()
    counter["you"] = 1
    stack = deque(node for node in all_nodes if not indegree_lookup[node])
    while stack:
        curr_node = stack.pop()
        curr_freq = counter[curr_node]
        for next_node in graph[curr_node]:
            counter[next_node] += curr_freq
            indegree_lookup[next_node] -= 1
            if not indegree_lookup[next_node]:
                stack.append(next_node)
    return counter['out']

print(a('./example.txt'))
print(a('./input.txt'))