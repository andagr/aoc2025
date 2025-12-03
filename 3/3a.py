lines = []
with open("input.txt", "r") as file:
    lines = [line.strip() for line in file]

selected_batteries = []
for line in lines:
    (max1, i) = sorted(
        [(int(line[i]), i) for i in range(0, len(line) - 1)],
        key=lambda n: n[0],
        reverse=True,
    )[0]
    max2 = max([int(c) for c in line[i + 1 :]])
    selected_batteries.append(int(str(max1) + str(max2)))

print(sum(selected_batteries))
