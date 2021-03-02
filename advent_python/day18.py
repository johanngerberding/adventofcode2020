TEST = """1 + 2 * 3 + 4 * 5 + 6
1 + (2 * 3) + (4 * (5 + 6))
2 * 3 + (4 * 5)
5 + (8 * 3 + 9 + 3 * 4 * 3)
5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))
((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"""

# number
# instruction

def parse(raw: str, part) -> list:
    lines = raw.split("\n")
    results = []
    for line in lines:
        if "(" in line:
            line = line[:]
            while ")" in line:
                # extract indexes of inner brackets
                close_idx = [i for i, char in enumerate(line) if char == ')'][0]
                open_idx = [i for i, char in enumerate(line) if char == '(' and i < close_idx][-1]
                # cut out expression in brackets
                exp = line[open_idx+1:close_idx]
                res = exec_ops(list(reversed(exp.split(" "))), part=part)
                line = line[:open_idx] + str(res) + line[close_idx+1:]
            results.append(exec_ops(list(reversed(line.split(" "))), part=part))
        else:
            ops = list(reversed(line.split(" ")))
            results.append(exec_ops(ops, part=part))
    
    return results
     
        
def exec_ops(ops: list, part) -> int:
    if part == 1:
        ops = ops.copy()
        curr = int(ops.pop())
        while ops:
            next_ops = [ops.pop() for _ in range(2)]
            if next_ops[0] == '+':
                curr += int(next_ops[1])
            elif next_ops[0] == '*':
                curr *= int(next_ops[1])
        
        return curr

    elif part == 2:
        ops = ops.copy()

        while "+" in ops:
            idx = ops.index("+")
            res = int(ops[idx-1]) + int(ops[idx+1])
            ops = ops[:idx-1] + [res] + ops[idx+2:]
        while "*" in ops:
            idx = ops.index("*")
            res = int(ops[idx-1]) * int(ops[idx+1])
            ops = ops[:idx-1] + [res] + ops[idx+2:]
        
        assert len(ops) == 1

        return int(ops[0])
        


test = """1 + (2 * 3) + (4 * (5 + 6))
2 * 3 + (4 * 5)
5 + (8 * 3 + 9 + 3 * 4 * 3)
5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))
((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"""

res = parse(test, part=2)
print(res)


print(parse(TEST, part=1))

with open("../inputs/day18.txt") as f:
    data = f.read()
    results = parse(data, part=1)
    print(sum(results))
    results_2 = parse(data, part=2)
    print(sum(results_2))