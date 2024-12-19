from collections import defaultdict, deque

def a(filename: str):
    with open(filename) as file:
        line = file.readline()
    block_sizes = [int(digit) for digit in line]
    total_space = sum(block_sizes)
    # print(f"total space: {total_space}")
    disk = [0] * total_space
    free_spaces = deque()
    file_spaces = deque()
    pos = 0
    file_id = 0
    is_file = True
    for block_size in block_sizes:
        if is_file:
            for _ in range(block_size):
                disk[pos] = file_id
                file_spaces.append(pos)
                pos += 1
            file_id += 1
        else:
            free_spaces.extend(range(pos, pos + block_size))
            pos += block_size
        is_file = not is_file
    # print(disk)
    # print(free_spaces)
    while file_spaces and free_spaces:
        pos = file_spaces.pop()
        file_id = disk[pos]
        free_space_pos = free_spaces.popleft()
        if free_space_pos >= pos:
            break
        disk[pos] = 0
        disk[free_space_pos] = file_id
        # print(f"{file_id} moved to {free_space_pos}")
    # print(disk)
    return sum(pos * file_id for pos, file_id in enumerate(disk))

filename = "example.txt"
filename2 = "input.txt"
print(a(filename))
print(a(filename2))