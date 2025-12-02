from bisect import bisect_left, bisect_right
from itertools import accumulate, count


def b(filename: str):
    sorted_intervals = []
    with open(filename) as file:
        intervals = file.readline().split(',')
    for interval in intervals:
        start, end = interval.split('-')
        sorted_intervals.append([int(start), int(end)])
    sorted_intervals.sort()
    max_val = sorted_intervals[-1][-1]
    max_digit_count = len(str(max_val))

    res = 0
    seen = set()
    for repeats in range(2, max_digit_count + 1):
        invalid_ids = []
        for first_half in count(1):
            total = int(str(first_half) * repeats)
            invalid_ids.append(total)
            if len(invalid_ids) >= 2 and invalid_ids[-2] >= max_val:
                break
        
        for start, end in sorted_intervals:
            sp = bisect_left(invalid_ids, start)
            ep = bisect_right(invalid_ids, end) - 1
            for pos in range(sp, ep + 1):
                num = invalid_ids[pos]
                if num in seen:
                    continue
                seen.add(num)
                res += num
    return res

print(b('./example.txt'))
print(b('./input.txt'))