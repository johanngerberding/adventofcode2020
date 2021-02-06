import string
from typing import List, NamedTuple, Dict
from collections import defaultdict
import re

TEST = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.
"""

TEST_2 = """shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags."""


class Bag(NamedTuple):
    color: str
    contains: Dict[str, int]


def parse_line(line: str) -> Bag:
    p1, p2 = line.split(" contain ")
    color = p1[:-5]
    p2 = p2.rstrip(".")
    if p2 == "no other bags":
        return Bag(color, {})
    
    bags = {}
    components = p2.split(", ")
    for component in components:
        component = re.sub(r"bags?$", "", component)
        space = component.find(" ")
        count = int(component[:space].strip())
        color_ = component[space:].strip()
        bags[color_] = count
    
    return Bag(color, bags)


def create_bag_list(inp: str) -> List[Bag]:
    return [parse_line(line) for line in inp.splitlines()]


def parents(bags: List[Bag]) -> Dict[str, List[str]]:
    ic = defaultdict(list)
    for bag in bags:
        for child in bag.contains:
            ic[child].append(bag.color)
    
    return ic


def can_contain(bags: List[Bag], color: str) -> List[str]:
    parent_map = parents(bags)
    check_color = [color]
    contain = set()

    while check_color:
        child = check_color.pop()
        for parent in parent_map.get(child, []):
            if parent not in contain:
                contain.add(parent)
                check_color.append(parent)
    
    return list(contain)

    

assert len(can_contain(create_bag_list(TEST), 'shiny gold')) == 4


def number_bags_inside(bags: List[Bag], color: str) -> int:
    # create dictionary of bags by color
    bags_color = {bag.color: bag for bag in bags}
    number_bags = 0
    stack: List[Tuple[str, int]] = [(color, 1)]
    while stack:
        next_color, mult = stack.pop()
        bag = bags_color[next_color]
        for child, count in bag.contains.items():
            number_bags += mult * count
            stack.append((child, count * mult))

    return number_bags


assert number_bags_inside(create_bag_list(TEST_2), "shiny gold") == 126

with open('../inputs/day07.txt', 'r') as f:
    txt = f.read()
    bags = create_bag_list(txt)
    print(len(can_contain(bags, 'shiny gold')))
    print(number_bags_inside(bags, 'shiny gold'))


# down below my noob code, solved the first part on my own, 
# the second I didn't have had the patience and look at the joel grus github 
# (https://github.com/joelgrus/advent2020/blob/master/advent2020/day07.py)

"""

def calc_num_bags(input_string: str, search_col='shiny gold') -> int:
    # remove punctutation
    data = [line.strip().translate(str.maketrans('', '', string.punctuation)) for line in input_string.splitlines()]
    # list of words to cut out
    el_words = ['bags', 'contain', 'bag']

    comps = dict()

    for i in range(len(data)):
        words = data[i].split()
        result_words = [word for word in words if word.lower() not in el_words]
        goal = ' '.join(result_words[:2])
        components = []
        if len(result_words[2:]) == 2:
            comps[goal] = 'no other'
        elif len(result_words[2:]) > 2:
            assert(len(result_words[2:]) % 3 == 0)
            for j in range(2, len(result_words[2:]), 3):
                color = ' '.join(result_words[j+1:j+3])
                components.append(color)
            comps[goal] = components

    bags = set()
    search_color=[search_col]

    while len(search_color) > 0:
        for key in comps.keys():
            if search_color[0] in comps[key]:
                bags.add(key)
                search_color.append(key)
        search_color = search_color[1:]

    return len(bags)

assert calc_num_bags(TEST) == 4

def calc_num_bags_2(input_string: str, search_col='shiny gold') -> int:
    # remove punctutation
    data = [line.strip().translate(str.maketrans('', '', string.punctuation)) for line in input_string.splitlines()]
    # list of words to cut out
    el_words = ['bags', 'contain', 'bag']

    comps = dict()

    for i in range(len(data)):
        words = data[i].split()
        result_words = [word for word in words if word.lower() not in el_words]
        goal = ' '.join(result_words[:2])
        components = []
        if len(result_words[2:]) == 2:
            comps[goal] = 'no other'
        elif len(result_words[2:]) > 2:
            assert(len(result_words[2:]) % 3 == 0)
            for j in range(2, len(result_words[2:]), 3):
                num = int(result_words[j])
                color = ' '.join(result_words[j+1:j+3])
                components.append((color, num))
            comps[goal] = components

    print(comps)
    num = 1
    search_bag = [search_col]
    while len(search_bag) > 0:
        components = comps[search_bag[0]]
        if type(components) == list: 
            for comp in components:
                num *= comp[1]
                search_bag.append(comp[0])
        search_bag = search_bag[1:]

    print(num)
    print(search_bag)
    return 0


calc_num_bags_2(TEST_2)


    print(calc_num_bags(txt))

"""