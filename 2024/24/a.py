from operator import and_, or_, xor
from typing import Counter, Dict, List, Tuple
from collections import Counter, defaultdict, deque
from math import inf
AND = 'AND'
OR = 'OR'
XOR = 'XOR'
operation_lookup = {
    AND: and_,
    OR: or_,
    XOR: xor
}

def a(filename_values: str, filename_wires: str):
    value_lookup = {}
    with open(filename_values) as file:
        while line := file.readline():
            wire, value = line.split(": ")
            value_lookup[wire] = int(value)
    
    prereq_lookup = {}
    parent_lookup = defaultdict(list)
    indegree_lookup = Counter()
    with open(filename_wires) as file:
        while line := file.readline():
            line = line.rstrip()
            input, output = line.split(" -> ")
            input1, operation, input2 = input.split()
            prereq_lookup[output] = (input1, input2, operation)
            parent_lookup[input1].append(output)
            parent_lookup[input2].append(output)
            indegree_lookup[output] += 2
    
    stack = deque(wire for wire in value_lookup if not indegree_lookup[wire])
    while stack:
        curr = stack.pop()
        if curr in prereq_lookup:
            prev1, prev2, operation_name = prereq_lookup[curr]
            val1 = value_lookup[prev1]
            val2 = value_lookup[prev2]
            op = operation_lookup[operation_name]
            value_lookup[curr] = op(val1, val2)
        for parent in parent_lookup[curr]:
            indegree_lookup[parent] -= 1
            if not indegree_lookup[parent]:
                stack.append(parent)
    wires_sorted = sorted(((wire, value) for wire, value in value_lookup.items() if wire[0] == 'z'), reverse=True)
    res = 0
    for wire, value in wires_sorted:
        res = res << 1 | value
    return res
        

# print(a('example_values.txt', 'example_wires.txt'))
# print(a('example_values2.txt', 'example_wires2.txt'))
# print(a('input_values.txt', 'input_wires.txt'))
res = a('input_values_test.txt', 'input_wires_fix.txt')
last_flag = res & -res
print(bin(res))
print(last_flag.bit_length() - 1)