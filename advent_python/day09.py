
TEST = """35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576
"""


stream = [int(line) for line in TEST.strip().split("\n")]
len_preamble = 5


def valid_number(stream: list, len_preamble: int, pos: int) -> bool:
    preamble = stream[pos-len_preamble:pos]
    val = stream[pos]
    for i in range(len_preamble-1):
        for j in range(i+1, len_preamble):
            if preamble[i]+preamble[j] == val:
                return True
    return False


def check_stream(stream: list, len_preamble: int) -> int:
    for i in range(len_preamble, len(stream)):
        if valid_number(stream, len_preamble, i):
            continue
        else:
            return stream[i]
    return -1


assert check_stream(stream, len_preamble) == 127


def find_contiguous_numbers(stream: list, val: int) -> int:
    # sliding window with increasing window size
    for i in range(2, len(stream)):
        for j in range(len(stream) - i):
            contiguous_sum = sum(stream[j:j+i])
            if contiguous_sum == val:
                return min(stream[j:j+i]) + max(stream[j:j+i])

    return -1

assert find_contiguous_numbers(stream, 127) == 62

with open("../inputs/day09.txt") as f: 
    data = f.read()
    stream = [int(line) for line in data.strip().split("\n")]
    len_preamble = 25
    val = check_stream(stream, len_preamble)
    print(val)
    print(find_contiguous_numbers(stream, val))