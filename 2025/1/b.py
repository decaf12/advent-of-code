def b(filename: str):
    curr = 50
    res = 0
    with open(filename) as file:
        while line := file.readline():
            dir = line[0]
            cycle_count, steps = divmod(int(line[1:]), 100)
            res += cycle_count
            if dir == 'L':
                if curr > steps:
                    curr -= steps
                else:
                    if curr:
                        res += 1
                    curr = (curr - steps) % 100
            else:
                if curr + steps < 100:
                    curr += steps
                else:
                    if curr:
                        res += 1
                    curr += steps - 100
    return res


print(b('./example.txt'))
print(b('./input.txt'))