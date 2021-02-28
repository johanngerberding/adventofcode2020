from __future__ import annotations
from typing import Dict, List, NamedTuple, Tuple
import math 

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

# my first bullshit code, it's pretty ugly but it works for the first part of the problem
""" def validate_tickets(raw: str) -> list:
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

with open('../inputs/day16.txt') as f: 
    nums = validate_tickets(f.read())
    print(sum(nums))

 """

# second attempt, more object oriented (check out Joel Grus github! it's based on that)



Range = Tuple[int, int]

def make_range(raw: str) -> Range:
    low, high = raw.split("-")
    return (int(low), int(high))


class Rule(NamedTuple):
    name: str 
    ranges: Tuple[Range, Range]

    def is_valid(self, i: int) -> bool:
        return any(lo <= i <= hi for lo, hi in self.ranges)

    @staticmethod
    def parse(line: str) -> Rule:
        name, ranges = line.split(": ")
        r1, r2 = ranges.split(" or ")
        return Rule(name=name, ranges=(make_range(r1), make_range(r2)))


Ticket = List[int]

def make_ticket(raw: str) -> Ticket:
    return [int(n) for n in raw.split(",")]


class Problem(NamedTuple):
    rules: List[Rule]
    your_ticket: Ticket
    nearby_tickets: List[Ticket]


    def valid_for_any_field(self, i: int) -> bool:
        return any(rule.is_valid(i) for rule in self.rules)

    
    def is_invalid(self, ticket: Ticket) -> bool:
        for num in ticket:
            if not self.valid_for_any_field(num):
                return True
        
        return False

    
    def error_rate(self) -> int:
        return sum(num 
                   for ticket in self.nearby_tickets 
                   for num in ticket 
                   if not self.valid_for_any_field(num))

    
    def discard_invalid_tickets(self) -> Problems:
        valid_tickets = [t for t in self.nearby_tickets if not self.is_invalid(t)]
        return self._replace(nearby_tickets=valid_tickets)


    @staticmethod
    def parse(raw: str) -> Problem:
        a, b, c = raw.split("\n\n")
        b = b.split("\n")[-1]

        rules = [Rule.parse(line) for line in a.split("\n")]
        my_ticket = make_ticket(b)
        nearby_tickets = [make_ticket(line) for line in c.split("\n")[1:]]

        return Problem(rules, my_ticket, nearby_tickets)


def identify_fields(problem: Problem) -> List[str]:
    num_fields = len(problem.your_ticket)
    tickets = [problem.your_ticket] + problem.nearby_tickets

    candidates = [
        {rule for rule in problem.rules
        if all(rule.is_valid(ticket[i]) for ticket in tickets)} 
        for i in range(num_fields)
    ]

    while True:
        unique_rules = [rule for cand in candidates if len(cand) == 1 for rule in cand]
        if len(unique_rules) == num_fields:
            return [rule.name for cand in candidates for rule in cand]
        
        for i in range(num_fields):
            cand = candidates[i]
            if len(cand) > 1:
                cand = {rule for rule in cand if rule not in unique_rules}
                candidates[i] = cand


TEST_2 = """class: 0-1 or 4-19
row: 0-5 or 8-19
seat: 0-13 or 16-19

your ticket:
11,12,13

nearby tickets:
3,9,18
15,1,5
5,14,9"""

PROBLEM = Problem.parse(TEST)
assert PROBLEM.error_rate() == 71

PROBLEM_2 = PROBLEM.discard_invalid_tickets()

assert PROBLEM_2.nearby_tickets == [[7, 3, 47]]

with open("../inputs/day16.txt") as f:
    raw = f.read()
    problem = Problem.parse(raw)
    print(problem.error_rate())

    problem_2 = problem.discard_invalid_tickets()
    fields = identify_fields(problem_2)

    departure_values = [
        num for name, num in zip(fields, problem_2.your_ticket) if name.startswith("departure")
    ]
    assert len(departure_values) == 6
    prod = 1
    for val in departure_values:
        prod *= val 

    print(prod)