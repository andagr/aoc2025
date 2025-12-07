lines = []
with open("input.txt", "r") as file:
    lines = [line.strip() for line in file]

fresh_ranges = []
for line in lines:
    if line != '':
        fresh_ranges.append((int(line.split('-')[0]), int(line.split('-')[1])))
    else:
        break

fresh_ranges.sort()

fresh_ranges_excl = [fresh_ranges[0]]
(_, highest) = fresh_ranges[0]
for i in range(1, len(fresh_ranges)):
    (curr_l, curr_h) = fresh_ranges[i]
    (_, prev_h) = fresh_ranges[i - 1]
    if highest < curr_h:
        if highest >= curr_l:
            fresh_ranges_excl.append((highest + 1, curr_h))
        else:
            fresh_ranges_excl.append((curr_l, curr_h))
        highest = curr_h

print(sum([h - l + 1 for (l, h) in fresh_ranges_excl]))