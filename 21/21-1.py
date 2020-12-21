filename = 'words'

with open(filename, 'r') as f:
    i = f.readlines()

all_ingredients = set()
all_allergies = set()
class Item:
    def __init__(self, input):
        i, _, allergy = input.partition(' (contains ')
        allergy = allergy.strip().strip(')')
        self.ingredients = set(i.split())
        self.allergies = set(allergy.split(', '))
    def __str__(self):
        return f'ingredients:{len(self.ingredients)} allergies:{len(self.allergies)}'
    def __repr__(self):
        return str(self)

items = []
allergies = {}
for line in i:
    item = Item(line)
    all_ingredients |= item.ingredients
    all_allergies |= item.allergies
    items.append(item)
print(all_allergies)
print(all_ingredients)
print()

possible_allergies = set()
for a in all_allergies:
    common_ingredients = all_ingredients.copy()
    for item in items:
        if a in item.allergies:
            common_ingredients &= item.ingredients
    allergies[a] = common_ingredients
    possible_allergies |= common_ingredients

final = all_ingredients - possible_allergies
"""
for k,v in allergies.items():
    print(k,v)
print(final)
"""
count = 0
for item in items:
    count += sum(i in item.ingredients for i in final)
print(count)
