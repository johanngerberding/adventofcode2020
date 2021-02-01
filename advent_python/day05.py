TEST_INPUTS = [
    'BFFFBBFRRR',
    'FFFBBBFRRR',
    'BBFFBBFRLL'
]

TEST_RESULTS = [
    567,
    119,
    820
]

# range 0,127
# F -> lower
# B -> upper
def get_row(boarding_pass: str) -> int:
    rows = boarding_pass[:7]
    row_range = list(range(128))
    for i in rows:
        m = len(row_range) // 2
        if i == 'F':
            row_range = row_range[:m]
        elif i == 'B':
            row_range = row_range[m:]
    assert len(row_range) == 1
    return row_range[0]


# range 0, 7
# R -> upper
# L -> lower
def get_col(boarding_pass: str) -> int:
    cols = boarding_pass[7:]
    col_range = list(range(8))
    for i in cols:
        m = len(col_range) // 2
        if i == 'R':
            col_range = col_range[m:]
        elif i == 'L':
            col_range = col_range[:m]
    assert len(col_range) == 1
    return col_range[0]

def get_ID(boarding_pass: str) -> int:
    col = get_col(boarding_pass)
    row = get_row(boarding_pass)
    return row * 8 + col


for test, result in zip(TEST_INPUTS, TEST_RESULTS):
    assert(get_ID(test) == result)

with open("../inputs/day05.txt") as f:
    data = [l.strip() for l in f]
    max_ID = 0
    for boarding_pass in data:
        if get_ID(boarding_pass) > max_ID:
            max_ID = get_ID(boarding_pass)
    
    print(max_ID)