from typing import List
REGISTER_A = 0
REGISTER_B = 0
REGISTER_C = 0

def combo_lookup(operand: int):
    if operand <= 3:
        return operand
    if operand == 4:
        return REGISTER_A
    if operand == 5:
        return REGISTER_B
    if operand == 6:
        return REGISTER_C
    raise Exception('fail')

def adv(operand: int, ic: int):
    global REGISTER_A
    numerator = REGISTER_A
    denominator = 1 << combo_lookup(operand)
    REGISTER_A = numerator // denominator
    return ic + 2, -1

def bxl(operand: int, ic: int):
    global REGISTER_B
    REGISTER_B ^= operand
    return ic + 2, -1

def bst(operand: int, ic: int):
    global REGISTER_B
    REGISTER_B = combo_lookup(operand) & 0b111
    return ic + 2, -1

def jnz(operand: int, ic: int):
    if not REGISTER_A:
        return ic + 2, -1
    return operand, -1

def bxc(operand: int, ic: int):
    global REGISTER_B
    REGISTER_B ^= REGISTER_C
    return ic + 2, -1

def out(operand: int, ic: int):
    output = combo_lookup(operand) & 0b111
    return ic + 2, output

def bdv(operand: int, ic: int):
    global REGISTER_B
    numerator = REGISTER_A
    denominator = 1 << combo_lookup(operand)
    REGISTER_B = numerator // denominator
    return ic + 2, -1

def cdv(operand: int, ic: int):
    global REGISTER_C
    numerator = REGISTER_A
    denominator = 1 << combo_lookup(operand)
    REGISTER_C = numerator // denominator
    return ic + 2, -1

instruction_table = [adv, bxl, bst, jnz, bxc, out, bdv, cdv]

def a(filename: str):
    global REGISTER_A, REGISTER_B, REGISTER_C
    with open(filename) as file:
        line_a = file.readline()
        _, a_val = line_a.split(": ")
        REGISTER_A = int(a_val)
        
        line_b = file.readline()
        _, b_val = line_b.split(": ")
        REGISTER_B = int(b_val)
        
        line_c = file.readline()
        _, c_val = line_c.split(": ")
        REGISTER_C = int(c_val)

        file.readline()

        line_program = file.readline()
        _, program = line_program.split(": ")
        instructions = [int(instruction) for instruction in program.split(",")]
    
    n = len(instructions)
    output = []
    ic = 0
    while ic in range(n):
        instruction = instructions[ic]
        operand = instructions[ic + 1] if ic < n - 1 else 0
        execution = instruction_table[instruction]
        next_ic, instruction_output = execution(operand, ic)
        if instruction_output != -1:
            output.append(instruction_output)
        ic = next_ic
    return ",".join(str(instruction_output) for instruction_output in output)
 
print(a('example.txt'))
print(a('input.txt'))