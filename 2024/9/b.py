from collections import defaultdict, deque

def b(filename: str):
    with open(filename) as file:
        line = file.readline()
    block_sizes = [int(digit) for digit in line]
    total_space = sum(block_sizes)
    disk = [0] * total_space
    free_blocks = []
    file_blocks = deque()
    pos = 0
    file_id = 0
    is_file = True
    for block_size in block_sizes:
        if is_file:
            file_blocks.append((pos, block_size))
            for _ in range(block_size):
                disk[pos] = file_id
                pos += 1
            file_id += 1
        else:
            free_blocks.append((pos, block_size))
            pos += block_size
        is_file = not is_file
    # print(disk)
    while file_blocks and free_blocks:
        pos, block_size = file_blocks.pop()
        file_id = disk[pos]
        for block_id, (free_pos, free_block_size) in enumerate(free_blocks):
            if free_pos >= pos:
                break
            if free_block_size >= block_size:
                disk[free_pos:free_pos + block_size] = [file_id] * block_size
                disk[pos:pos + block_size] = [0] * block_size
                free_blocks[block_id] = (free_pos + block_size, free_block_size - block_size)
                # print(f"block of size {block_size} with value {file_id} moved from {pos} to {free_pos}")
                break
    # print(disk)
    return sum(pos * file_id for pos, file_id in enumerate(disk))

filename = "example.txt"
filename2 = "input.txt"
print(b(filename))
print(b(filename2))