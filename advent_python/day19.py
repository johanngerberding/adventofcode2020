import re

TEST = """0: 4 1 5
1: 2 3 | 3 2
2: 4 4 | 5 5
3: 4 5 | 5 4
4: "a"
5: "b"

ababbb
bababa
abbbab
aaabbb
aaaabbb"""


def create_list(raw: str) -> list:
    raw = raw.split(' ')
    res = []
    for el in raw:
        if el.isdigit():
            res.append(int(el))
        else:
            res.append(el)

    return res


def read_input(raw: str):
    rules = {}
    base_elements = {}
    inp = raw.split("\n\n")
    inp = [line.split("\n") for line in inp]
    rules_list = inp[0]
    inp = inp[1]
    for rule in rules_list:
        num = int(rule.split(":")[0])
        val = rule.split(": ")[1]
        if '"' in val:
            val = val[1]
            base_elements[num] = val
        if "|" in val:
            val = "( " + val + " )"
        rules[num] = create_list(val)

    return inp, rules, base_elements


def check_string(elems: list) -> bool:
    for el in elems:
        if isinstance(el, int):
            return False
    return True


def flatten(l, a):
    for i in l:
        if isinstance(i, list):
            flatten(i, a)
        else:
            a.append(i)
    return a

def create_pattern(rules: dict, base_elements: dict) -> str:
    done = []
    _base_elements = {}
    while len(base_elements.keys()) < len(rules.keys()):
        for num, v in base_elements.items():
            if num not in done:
                for k, rule in rules.items():
                    while num in rule:
                        idx = rule.index(num)
                        rule[idx] = v
                    if check_string(rules[k]):
                        _base_elements[k] = rules[k]
            else:
                done.append(num)
        base_elements.update(_base_elements)
    
    pattern = flatten(rules[0], [])
    return ''.join(pattern)


with open("../inputs/day19.txt") as f: 
    inp, rules, base_elements = read_input(f.read())
    pattern = create_pattern(rules, base_elements)
  
    c = 0
    for line in inp:
        result = re.fullmatch(pattern, line)
        if result != None:
            c += 1
    
    print(c)
