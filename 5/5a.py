lines = []
with open("input.txt", "r") as file:
    lines = [line.strip() for line in file]

ranges = []
ids = []
isIngredients = False
for line in lines:
    if line == '': isIngredients = True
    if not isIngredients:
        ranges.append((int(line.split('-')[0]), int(line.split('-')[1])))
    elif line != '':
        ids.append(int(line))

fresh_ingredients = []
for id in ids:
    if any([id >= l and id <= h for (l, h) in ranges]):
        fresh_ingredients.append(id)

print(len(fresh_ingredients))