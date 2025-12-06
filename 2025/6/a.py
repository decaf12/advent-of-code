from math import prod


def a(filename: str):
    grid = []
    with open(filename) as file:
        while line := file.readline().rstrip():
            words = [word.strip() for word in line.split()]
            if words[0].isnumeric():
                grid.append([int(num) for num in words])
            else:
                operands = words
    res = 0
    for col, operand in zip(zip(*grid), operands):
        if operand == '*':
            res += prod(col)
        else:
            res += sum(col)
    return res

print(a('./example.txt'))
print(a('./input.txt'))