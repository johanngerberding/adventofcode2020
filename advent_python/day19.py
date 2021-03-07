from __future__ import annotations
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



def create_pattern_2(rules: dict, base_elements: dict) -> str:
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
                        if num == 8 or num == 11:
                            print(rules[num])
                            return 'Done'
                        _base_elements[k] = rules[k]
            else:
                done.append(num)
        base_elements.update(_base_elements)
    
    pattern = flatten(rules[0], [])
    return ''.join(pattern)


TEST_2 = """42: 9 14 | 10 1
9: 14 27 | 1 26
10: 23 14 | 28 1
1: "a"
11: 42 31
5: 1 14 | 15 1
19: 14 1 | 14 14
12: 24 14 | 19 1
16: 15 1 | 14 14
31: 14 17 | 1 13
6: 14 14 | 1 14
2: 1 24 | 14 4
0: 8 11
13: 14 3 | 1 12
15: 1 | 14
17: 14 2 | 1 7
23: 25 1 | 22 14
28: 16 1
4: 1 1
20: 14 14 | 1 15
3: 5 14 | 16 1
27: 1 6 | 14 18
14: "b"
21: 14 1 | 1 14
25: 1 1 | 1 14
22: 14 14
8: 42
26: 14 22 | 1 20
18: 15 15
7: 14 5 | 1 21
24: 14 1

abbbbbabbbaaaababbaabbbbabababbbabbbbbbabaaaa
bbabbbbaabaabba
babbbbaabbbbbabbbbbbaabaaabaaa
aaabbbbbbaaaabaababaabababbabaaabbababababaaa
bbbbbbbaaaabbbbaaabbabaaa
bbbababbbbaaaaaaaabbababaaababaabab
ababaaaaaabaaab
ababaaaaabbbaba
baabbaaaabbaaaababbaababb
abbbbabbbbaaaababbbbbbaaaababb
aaaaabbaabaaaaababaa
aaaabbaaaabbaaa
aaaabbaabbaaaaaaabbbabbbaaabbaabaaa
babaaabbbaaabaababbaabababaaab
aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba"""


""" 
with open("../inputs/day19.txt") as f: 
    data = f.read()
    inp_1, rules_1, base_elements_1 = read_input(data)
    pattern_1 = create_pattern(rules_1, base_elements_1)
    
    c = 0
    for line in inp_1:
        result_1 = re.fullmatch(pattern_1, line)
        if result_1 != None:
            c += 1
    
    print(c)
 """

## PART 2 ##
# to be honest, I tried some stuff but nothing worked, so I looked here for a solution:
# https://github.com/joelgrus/advent2020/blob/master/advent2020/day19.py
# I like the explanations and the object oriented design (I am still pretty bad at OOD)


from typing import NamedTuple, List, Optional, Tuple, Iterator
from collections import deque 

class Rule(NamedTuple):
    id: int 
    literal: Optional[str] = None
    subrules: List[List[int]] = []

    @staticmethod
    def parse(line: str) -> Rule:
        rule_id, rest = line.strip().split(": ")
        if rest.startswith('"'):
            return Rule(id=int(rule_id), literal=rest[1:-1]) # base element
        
        if "|" in rest:
            parts = rest.split(" | ")
        else: 
            parts = [rest]
        
        return Rule(id=int(rule_id), subrules=[[int(n) for n in part.split()] for part in parts])


def check(s: str, rules: List[Rule]) -> bool:
    """Returns true if s matches rule 0"""
    # queue of pairs (remaining string, remaining rules)
    queue = deque([(s, [0])])

    while queue:
        #print(queue)
        # take one from the queue
        s, rule_ids = queue.popleft()

        # if no strings and no rules are left, you are done
        if not s and not rule_ids:
            return True 

        # if one is missing, this is a dead end, continue (part 2)
        elif not s or not rule_ids:
            continue 
        
        # each rule can match at most 1 character (so if we have more, than this isn't a match)
        elif len(rule_ids) > len(s):
            continue

        rule = rules[rule_ids[0]]
        rule_ids = rule_ids[1:]

        # first rule is literal, so if it matches the first character,
        # then add the rest of the string and the rest of the rules to the queue

        if rule.literal and s[0] == rule.literal:
            queue.append((s[1:], rule_ids))
        
        # otherwise I have one more sequences of subrules
        # for each of those sequences, I prepend it to the remaining rule_ids
        # and add that new list of rule ids to the queue with s 
        else: 
            for subrule_ids in rule.subrules:
                queue.append((s, subrule_ids + rule_ids))

    
    # queue is exhausted, never found a match, so return false 
    return False 


def parse(raw: str):
    rules, strings = raw.split("\n\n")
    rules = [Rule.parse(rr) for rr in rules.split("\n")]
    rules.sort()
    assert all(rule.id == i for i, rule in enumerate(rules))
    strings = strings.split("\n")
    return rules, strings 


RAW = """0: 4 1 5
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

RULES, STRINGS = parse(RAW)   
res = [check(s, RULES) for s in STRINGS]

with open('../inputs/day19.txt') as f:
    raw = f.read()
rules, strings = parse(raw)

# good = 0
# for i, s in enumerate(strings):
#     print(i, s)
#     if check(s, rules):
#         good += 1

# print(good)

# part 2
rules[8] = Rule.parse("8: 42 | 42 8")
rules[11] = Rule.parse("11: 42 31 | 42 11 31")

good = 0
for i, s in enumerate(strings):
    print(i, s)
    if check(s, rules):
        good += 1

print(good)