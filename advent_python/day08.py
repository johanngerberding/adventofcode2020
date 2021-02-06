TEST = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6
"""


def read_instructions(raw: str) -> dict:
    instructions = {}
    r_instructions = raw.splitlines()
    for i, instruction in enumerate(r_instructions):
        code, val = instruction.split(" ")
        instructions[i] = [code, int(val), 0]
        
    return instructions


def loop_instructions(inst: dict) -> int:
    instructions = inst
    acc = 0
    pos = 0
    while True:
        if instructions[pos][2] != 0:
            return acc
        else:
            instructions[pos][2] += 1
            if instructions[pos][0] == 'nop':
                pos += 1
            elif instructions[pos][0] == 'acc':
                acc += instructions[pos][1]
                pos += 1
            elif instructions[pos][0] == 'jmp':
                pos += instructions[pos][1]


assert loop_instructions(read_instructions(TEST)) == 5

with open('../inputs/day08.txt', 'r') as f:
    data = f.read()
    instructions = read_instructions(data)
    print(loop_instructions(instructions))