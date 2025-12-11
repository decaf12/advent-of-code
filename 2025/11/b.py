from collections import defaultdict, deque
from typing import Counter


def b(filename: str):
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
    
    indegree_copy = indegree_lookup.copy()
    tour = []
    stack = deque(node for node in all_nodes if not indegree_copy[node])
    while stack:
        curr_node = stack.pop()
        tour.append(curr_node)
        for next_node in graph[curr_node]:
            indegree_copy[next_node] -= 1
            if not indegree_copy[next_node]:
                stack.append(next_node)
    
    order = [node for node in tour if node == 'dac' or node == 'fft']
    
    def count_ways(start: str, end: str, start_ways: int):
        indegree_copy = indegree_lookup.copy()
        counter = Counter()
        counter[start] = start_ways
        stack = deque(node for node in all_nodes if not indegree_copy[node])
        while stack:
            curr_node = stack.pop()
            curr_freq = counter[curr_node]
            for next_node in graph[curr_node]:
                counter[next_node] += curr_freq
                indegree_copy[next_node] -= 1
                if not indegree_copy[next_node]:
                    stack.append(next_node)
        return counter[end]
    
    first, second = order
    svr_to_first = count_ways('svr', first, 1)
    first_to_second = count_ways(first, second, svr_to_first)
    second_to_out = count_ways(second, 'out', first_to_second)
    return second_to_out

# print(b('./example.txt'))
print(b('./input.txt'))