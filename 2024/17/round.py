def round(A: int):
    B = A & 0b111
    B ^= 0b10
    C = A >> B
    B ^= 0b111
    B ^= C
    A >>= 3
    return A, B & 0b111

sequence = [2,4,1,2,7,5,1,7,4,4,0,3,5,5,3,0]
sequence_reversed = sequence[::-1]

def tacos(target_A: int, target_B: int):
    candidates = []
    base = target_A << 3
    for A in range(base, base + 8):
        end_A, end_B = round(A)
        if (end_A, end_B) == (target_A, target_B):
            candidates.append(A)
    return candidates

def beef():
    candidates = [0]
    for target_B in sequence_reversed:
        next_candidates = []
        for target_A in candidates:
            next_candidates.extend(tacos(target_A, target_B))
        candidates = next_candidates
    return candidates

res = beef()
print(res)
print(min(res))