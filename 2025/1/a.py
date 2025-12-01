def a(filename: str):
    curr = 50
    res = 0
    with open(filename) as file:
        while line := file.readline():
            dir = line[0]
            steps = int(line[1:]) % 100
            if dir == 'L':
                curr = (curr - steps) % 100
            else:
                curr = (curr + steps) % 100
            if not curr:
                res += 1
    return res


print(a('./example.txt'))
print(a('./input.txt'))