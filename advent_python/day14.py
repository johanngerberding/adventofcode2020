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

    def load_instruction_2(self, instruction):
        if 'mask' in instruction:
            self.mask = instruction.split("= ")[1]
            self.mask = list(self.mask)
            assert len(self.mask) == 36
        elif 'mem' in instruction:
            pos = int(instruction.split("[")[1].split("]")[0])
            val = int(instruction.split("= ")[1])
            #val_str = list(str(to_binary(val)).zfill(36))
            pos_str = list(str(to_binary(pos)).zfill(36))
            result = pos_str[:]
            x_idx = []
            for i in range(len(self.mask)):
                if self.mask[i] == 'X':
                    result[i] = 'X'
                    x_idx.append(i)
                elif self.mask[i] == '1':
                    result[i] = '1'
            poss = []
            for i in range(2**len(x_idx)):
                num = list(str(to_binary(i)).zfill(len(x_idx)))
                poss.append(num)
            
            for el in poss:
                check = result[:]
                for n, idx in enumerate(x_idx):
                    check[idx] = el[n]
                self.memory[int("".join(check), 2)] = val



def read_input(raw: str) -> list:
    return [line.strip() for line in raw.splitlines()]


def to_binary(num: int) -> int:
    return int(bin(num)[2:])



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
        loader.load_instruction_2(inst)
    sum_vals = 0 
    for _, v in loader.memory.items():
        sum_vals += v 
    print(sum_vals)