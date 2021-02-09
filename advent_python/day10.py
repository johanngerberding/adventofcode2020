from itertools import compress, product

def combinations(items):
    return ( set(compress(items,mask)) for mask in product(*[[0,1]]*len(items)) )

test_list = [1,2,3,4,5]
print(len(list(combinations(test_list))))


TEST = """16
10
15
5
1
11
7
19
6
12
4
"""

TEST_2 = """28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3
"""

def read_input(raw: str) -> list:
    data = [int(line.strip()) for line in raw.splitlines()]
    data.append(0)
    data.append(max(data)+3)
    data = sorted(data)
    return data


def validate(data: list) -> bool:
    for i in range(len(data)-1):
        # validate the step, max 3
        step = data[i+1]-data[i]
        if step > 3:
            return False
    return True


def min_number_elements(raw: str) -> int:
    data = read_input(raw)
    return 0


min_number_elements(TEST)

"""
def count_arrangements(raw: str) -> int:
    data_ = read_input(raw)
    data = read_input(raw)
    count = 0   
    while validate(data):
        for i in range(len(data)):
            data_ = 
        
        count += 1
        

    return 0"""


def jolt_count(raw: str) -> int:
    data = read_input(raw)

    jolt_count_1 = 0
    jolt_count_2 = 0
    jolt_count_3 = 0

    for i in range(len(data)-1):
        # validate the step, max 3
        step = data[i+1]-data[i]
        if step <= 3:
            if step == 1:
                jolt_count_1 += 1
            elif step == 2:
                jolt_count_2 += 1
            elif step == 3:
                jolt_count_3 += 1
        else: 
            print("We have a porblem here")

    return jolt_count_1 * jolt_count_3


with open("../inputs/day10.txt") as f: 
    print(jolt_count(f.read()))
