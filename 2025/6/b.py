from itertools import pairwise
from math import prod
from typing import List

def generate(subgrid: List[str]):
    for col in zip(*subgrid):
        yield int("".join(col))

def b(filename: str):
    lines = []
    with open(filename) as file:
        while line := file.readline().rstrip('\n'):
            if line[0] == '*' or line[0] == '+':
                operands = line
            else:
                lines.append(line)
    
    number_starts = [pos for pos, char in enumerate(operands) if char != ' ']
    number_starts.append(len(operands) + 1)

    def tokenize(line: str):
        return [line[prev: curr - 1] for prev, curr in pairwise(number_starts)]
    
    tokenized_lines = [tokenize(line) for line in lines]
          
    res = 0

    for col, operand in zip(zip(*tokenized_lines), operands.split()):
       if operand == '*':
           res += prod(generate(col))
       else:
           res += sum(generate(col))
    return res

print(b('./example.txt'))
print(b('./input.txt'))