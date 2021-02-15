TEST = """mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0"""


class Loader:
    def __init__(self):
        self.mask = ""
        self.memory = {}

    def load_instruction(self, instruction):
        if 'mask' in instruction:
            self.mask = instruction.split("= ")[1]
            self.mask = list(self.mask)
            assert len(self.mask) == 36
        elif 'mem' in instruction:
            pos = int(instruction.split("[")[1].split("]")[0])
            val = int(instruction.split("= ")[1])
            val_str = list(str(to_binary(val)).zfill(36))
            for i in range(len(self.mask)):
                if self.mask[i] == '0':
                    val_str[i] = '0'
                elif self.mask[i] == '1':
                    val_str[i] = '1'
            self.memory[pos] = int("".join(val_str), 2)



def read_input(raw: str) -> list:
    return [line.strip() for line in raw.splitlines()]


def to_binary(num: int) -> int:
    return int(bin(num)[2:])


def to_decimal(num: int) -> int:
    return 0

data = read_input(TEST)
loader = Loader()
for inst in data:
    loader.load_instruction(inst)

sum_vals = 0
for _, v in loader.memory.items():
    sum_vals += v

assert sum_vals == 165

with open("../inputs/day14.txt") as f: 
    data = read_input(f.read())
    loader = Loader()
    for inst in data:
        loader.load_instruction(inst)
    sum_vals = 0 
    for _, v in loader.memory.items():
        sum_vals += v 
    print(sum_vals)