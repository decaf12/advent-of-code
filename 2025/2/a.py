from bisect import bisect_left, bisect_right
from itertools import accumulate, count


def a(filename: str):
    sorted_intervals = []
    with open(filename) as file:
        intervals = file.readline().split(',')
    for interval in intervals:
        start, end = interval.split('-')
        sorted_intervals.append([int(start), int(end)])
    sorted_intervals.sort()
    max_val = sorted_intervals[-1][-1]

    invalid_ids = []
    for first_half in count(1):
        total = int(f"{first_half}{first_half}")
        invalid_ids.append(total)
        if len(invalid_ids) >= 2 and invalid_ids[-2] >= max_val:
            break
    
    cumulative = list(accumulate(invalid_ids, initial=0))

    res = 0
    for start, end in sorted_intervals:
        sp = bisect_left(invalid_ids, start)
        ep = bisect_right(invalid_ids, end) - 1
        res += cumulative[ep + 1] - cumulative[sp]
    return res

print(a('./example.txt'))
print(a('./input.txt'))