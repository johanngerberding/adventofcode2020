import re

INPUT = """ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in"""


INPUT_2 = """pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719"""

VALIDATION_FIELDS = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

def create_passports(inputs: str) -> list:
    """create a list of passport dictionaries"""
    data = inputs.splitlines() + [""]
    passports = []
    passport = ""
    for el in data:
        if el == "":
            passports.append(passport)
            passport = ""
        else:
            passport += el + " "
    
    pps = []
    for pp in passports:
        pp = pp.strip()
        vals = pp.split(" ")
        pp_dict = {}
        for val in vals:
            key, value = tuple(val.split(":"))
            pp_dict[key] = value
        pps.append(pp_dict)
    
    return pps


def validate_passports(inputs: str, val_fields: list) -> int:
    passports = create_passports(inputs)
    valid = 0
    for pp in passports:
        valid += 1
        for field in val_fields:
            if field not in pp.keys():
                valid -= 1
                break
    return valid

assert validate_passports(INPUT, VALIDATION_FIELDS) == 2

def validate_passports_2(inputs: str, val_fields: list) -> int:
    passports = create_passports(inputs)
    valid = 0
    for pp in passports:
        valid += 1
        for field in val_fields:
            if field not in pp.keys():
                valid -= 1
                break
            if not validate_field(pp, field):
                valid -= 1
                break

    return valid


def validate_field(pp: dict, field: str):
    val = pp[field]
    if field == 'byr':
        return (1920 <= int(val) <= 2002)
    elif field == 'iyr':
        return (2010 <= int(val) <= 2020)
    elif field == 'eyr':
        return (2020 <= int(val) <= 2030)
    elif field == 'hgt':
        if 'cm' in val:
            return (150 <= int(val[:-2]) <= 193)
        elif 'in' in val:
            return (59 <= int(val[:-2]) <= 76)
        else:
            return False
    elif field == 'hcl':
        if re.match('#[a-f-0-9]{6,}', val):
            return True
        else:
            return False
    elif field == 'ecl':
        return (val in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'])
    elif field == 'pid':
        return (len(val) == 9)
    else:
        return False

assert validate_passports_2(INPUT_2, VALIDATION_FIELDS) == 4

with open('../inputs/day04.txt', 'r') as f:
    data = f.read()
    print("1. Round: {} valid passports.".format(validate_passports(data, VALIDATION_FIELDS)))
    print("2. Round: {} valid passports.".format(validate_passports_2(data, VALIDATION_FIELDS)))