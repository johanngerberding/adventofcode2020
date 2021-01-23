INPUT = [
    "1-3 a: abcde",
    "1-3 b: cdefg",
    "2-9 c: ccccccccc"
]


def check_passwords(passwords: list) -> int:
    valid_pws = 0
    for pw in passwords:
        pw = pw.strip()
        pw = pw.split(' ')
        pw_str = pw[2]
        min_c = int(pw[0].split('-')[0])
        max_c = int(pw[0].split('-')[1])
        c = str(pw[1][:-1])
        count_c = pw_str.count(c)
        if min_c <= count_c <= max_c:
            valid_pws += 1

    return valid_pws

assert check_passwords(INPUT) == 2


def check_passwords_new(passwords: list) -> int:
    valid_pws = 0
    for pw in passwords:
        pw = pw.strip()
        pw = pw.split(' ')
        pw_str = pw[2]
        pos_1 = int(pw[0].split('-')[0])
        pos_2 = int(pw[0].split('-')[1])
        c = str(pw[1][:-1])
        if ((pw_str[pos_1 - 1] == c) ^ (pw_str[pos_2 - 1] == c)):
            valid_pws += 1

    return valid_pws

assert check_passwords_new(INPUT) == 1

with open('../inputs/day02.txt', 'r') as f:
    data = [l for l in f]
    valid_pws = check_passwords(data)
    print(valid_pws) 
    valid_pws = check_passwords_new(data)
    print(valid_pws)  