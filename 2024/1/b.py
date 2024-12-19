from collections import Counter

def b(filename: str):
    counter1 = Counter()
    counter2 = Counter()
    with open(filename) as file:
        while line := file.readline():
            num1, num2 = map(int, line.split())
            counter1[num1] += 1
            counter2[num2] += 1
    return sum(freq1 * num1 * counter2[num1] for num1, freq1 in counter1.items() if num1 in counter2)

print(b('./example.txt'))
print(b('./input.txt'))