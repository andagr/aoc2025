lines = []
with open("input.txt", "r") as file:
    lines = [line.strip() for line in file]


def find_max_number(start, space_req, line):
    max = sorted(
        [(int(line[i]), i) for i in range(start, len(line) - (space_req - 1))],
        key=lambda n: n[0],
        reverse=True,
    )[0]
    return max


selected_batteries = []
for line in lines:
    length = 12
    prev_max_ix = -1
    highest_nums = []
    for i in range(0, length):
        (max, max_ix) = find_max_number(prev_max_ix + 1, length - i, line)
        prev_max_ix = max_ix
        highest_nums.append(str(max))
    selected_batteries.append(int("".join(highest_nums)))

print(sum(selected_batteries))
