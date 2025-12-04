floor = []
with open("input.txt", "r") as file:
    floor = [list(line.strip()) for line in file]

def get_pos_around(x, y):
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            ax = x + dx
            ay = y + dy
            if (ay == y and ax == x or 
                ay < 0 or
                ax < 0 or
                ay >= len(floor) or
                ax >= len(floor[ay])):
                continue
            yield (x + dx, y + dy)

accessible_rolls = 0
for y in range(0, len(floor)):
    for x in range(0, len(floor[y])):
        if floor[y][x] != '@':
            continue
        surrounding_roll_count = 0
        for (ax, ay) in get_pos_around(x, y):
            if floor[ay][ax] == '@':
                surrounding_roll_count += 1
        if surrounding_roll_count < 4:
            accessible_rolls += 1

print(accessible_rolls)