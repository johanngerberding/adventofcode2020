TEST = """class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12"""

def validate_tickets(raw: str) -> list:
    invalid_numbers = []
    rules_dict, ticket, nearby = read_input(raw)

    min_max = []
    for _, v in rules_dict.items():
        ranges = v.split(' or ')
        for r in ranges:
            min_max.append([int(i) for i in r.split('-')])

    for el in nearby:
        for num in el:
            c = 0
            for rule in min_max:
                if num >= rule[0] and num <= rule[1]:
                    c += 1
            
            if c == 0:
                invalid_numbers.append(num)

    return invalid_numbers
 

def read_input(raw: str):
    data = raw.splitlines()
    rules = []
    ticket= []
    nearby = []

    c = 0
    for el in data:
        if el == '':
            c += 1
        else:
            if c == 0:
                rules.append(el)
            elif c == 1: 
                ticket.append(el)
            elif c == 2: 
                nearby.append(el)
    
    rules_dict = {}
    for rule in rules:
        field = rule[:rule.index(':')]
        ranges = rule[rule.index(':')+2:]
        rules_dict[field] = ranges

    ticket = ticket[1:]
    assert len(ticket) == 1
    ticket = [int(i) for i in ticket[0].split(',')]
    nearby_ = nearby[1:]
    nearby = []
    for el in nearby_:
        nearby.append([int(i) for i in el.split(',')])
    
    return rules_dict, ticket, nearby


nums = validate_tickets(TEST)
print(sum(nums))

with open('../inputs/day16.txt') as f: 
    nums = validate_tickets(f.read())
    print(sum(nums))
