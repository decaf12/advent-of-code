from scipy.optimize import linprog

def b(filename: str):
    res = 0
    with open(filename) as file:
        while line := file.readline().rstrip():
            switch_vals, target_vals = parse(line)
            machine_count = len(target_vals)
            switch_count = len(switch_vals)
            matrix = [[0 for _ in range(switch_count)] for _ in range(machine_count)]
            for switch_id, switch in enumerate(switch_vals):
                for machine_id in switch:
                    matrix[machine_id][switch_id] = 1
            c = [1] * switch_count
            sol = linprog(c, A_eq=matrix, b_eq=target_vals, integrality=[1] * switch_count)
            subtotal = sum(sol.x)
            res += subtotal
    return res

def parse(line: str):
    end_square_bracket_pos = line.find(']')

    first_brace_pos = line.find('{')
    target_joltages = line[first_brace_pos + 1:-1]
    target_vals = parse_joltages(target_joltages)

    middle = line[end_square_bracket_pos + 1: first_brace_pos - 1]
    switches = middle.split()
    switch_vals = [parse_switches(switch) for switch in switches]
    return switch_vals, target_vals

def parse_switches(switch: str):
    switch = switch[1: -1]
    return list(map(int, switch.split(',')))

def parse_joltages(input: str):
    return list(map(int, input.split(',')))

print(b('./example.txt'))
print(b('./input.txt'))