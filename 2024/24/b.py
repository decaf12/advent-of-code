from operator import and_, or_, xor
from typing import Counter, Dict, List, Tuple
from collections import Counter, defaultdict, deque
from math import inf

from numpy import str_
AND = 'AND'
OR = 'OR'
XOR = 'XOR'
operation_lookup = {
    AND: and_,
    OR: or_,
    XOR: xor
}

def b(filename_values: str, filename_wires: str):
    value_lookup = {}
    str_lookup = {}
    with open(filename_values) as file:
        while line := file.readline():
            wire, value = line.split(": ")
            value_lookup[wire] = int(value)
            str_lookup[wire] = wire
    
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
            prev1, prev2 = sorted((prev1, prev2))
            val1 = value_lookup[prev1]
            val2 = value_lookup[prev2]
            op = operation_lookup[operation_name]
            value_lookup[curr] = op(val1, val2)
            str1 = str_lookup[prev1]
            str2 = str_lookup[prev2]
            str1, str2 = sorted((str1, str2), key=lambda x: (-len(x), x), reverse=True)
            str_lookup[curr] = f"({str1} {operation_name} {str2})"
        for parent in parent_lookup[curr]:
            indegree_lookup[parent] -= 1
            if not indegree_lookup[parent]:
                stack.append(parent)
    for wire, str in sorted(str_lookup.items()):
        if wire[0] != 'z':
            continue
        print(f"{wire}: {str}")

# print(b('example_values.txt', 'example_wires.txt'))
# print(b('example_values2.txt', 'example_wires2.txt'))
print(b('input_values.txt', 'input_wires_fix.txt'))