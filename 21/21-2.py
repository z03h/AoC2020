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
#print(all_allergies)
#print(all_ingredients)
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
found_allergies = set()
final_allergies = {}
#"""
for k,v in sorted(allergies.items(), key=lambda t: len(t[1])):
    print(k,v)

for _ in range(len(all_allergies)):
    for a, iss in allergies.items():
        temp = iss - found_allergies
        #print(a, temp)
        if len(temp) == 1:
            iss = list(temp)[0]
            found_allergies.add(iss)
            final_allergies[a] = iss
            break
    print("--------")
print()
print(','.join(t[1] for t in sorted(final_allergies.items(), key=lambda t: t[0])))
#"""

