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

VALIDATION_FIELDS = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

def create_passports(input: str) -> list:
    """create a list of passport dictionaries"""
    passports = []
    passport = {}


def validate_passports(passports: list, val_fields: list) -> int:
    valid = 0
    for pp in passports:
        valid += 1
        for field in val_fields:
            if field not in pp:
                valid -= 1 
                break

    return valid

#assert validate_passports(INPUT, VALIDATION_FIELDS) == 2

with open('../inputs/day04.txt', 'r') as f:
    data = f.read()
    test = INPUT.splitlines()
    test = test + [""]
    passports = []
    passport = ""
    for el in test:
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
            print(tuple(val.split(":")))
            key, value = tuple(val.split(":"))
            pp_dict[key] = value
        pps.append(pp_dict)

    print(pps[0])
    


    