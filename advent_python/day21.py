from typing import NamedTuple, List  

class Food(NamedTuple):
    ingredients: List[str]
    allergens: List[str]

    def parse(raw: str):
        ingredients = raw.split("(")[0].strip().split(" ")
        allergens = raw.split("(")[1].replace(")","").replace("contains","").strip().split(", ")
        return Food(ingredients, allergens)


TEST = """mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)"""

data = TEST.splitlines()
foods = [Food.parse(el) for el in data]

allergens = set([allergen for food in foods for allergen in food.allergens])
allergens_dict = {a: [] for a in allergens}

for food in foods:
    for k, v in allergens_dict.items():
        if k in food.allergens:
            allergens_dict[k].append(set(food.ingredients))

allergens = {}
for k, v in allergens_dict.items():
    possible_vals = v.pop(0)
    for s in v:
        possible_vals.intersection_update(s)
    allergens[k] = possible_vals
    
all_ingredients = [el for food in foods for el in food.ingredients]
all_allergens = set()
for v in allergens.values():
    all_allergens.update(v)

diff = [el for el in all_ingredients if el not in all_allergens]
assert len(diff) == 5

with open("../inputs/day21.txt") as f:
    lines = f.read()

data = lines.splitlines()
foods = [Food.parse(el) for el in data]

allergens = set([allergen for food in foods for allergen in food.allergens])
allergens_dict = {a: [] for a in allergens}

for food in foods:
    for k, v in allergens_dict.items():
        if k in food.allergens:
            allergens_dict[k].append(set(food.ingredients))

allergens = {}
for k, v in allergens_dict.items():
    possible_vals = v.pop(0)
    for s in v:
        possible_vals.intersection_update(s)
    allergens[k] = possible_vals

    
all_ingredients = [el for food in foods for el in food.ingredients]
all_allergens = set()
for v in allergens.values():
    all_allergens.update(v)

diff = [el for el in all_ingredients if el not in all_allergens]
print(len(diff))

alls = {}
while len(alls) < len(allergens):
    for k, v in allergens.items():
        if len(list(v)) == 1:
            alls[k] = list(v)[0]

    for k, v in alls.items():
        for key, val in allergens.items():
            if key != k and v in list(val):
                val.remove(v)
            

keys = sorted([k for k in alls.keys()])
res = ','.join([alls[k] for k in keys])
print(res)