import re

lines = [line for line in open("input.txt", mode="r")]

regions = [
    (int(m.group(1)), int(m.group(2)), [int(c) for c in m.group(3).split(" ")])
    for line in lines
    if (m := re.match(r"^(\d+)x(\d+): (.+)$", line))
]


def fits(region):
    r_w, r_h = region[0:2]
    avail_space = (r_w / 3) * (r_h / 3)
    used_space = sum(region[2])
    return avail_space >= used_space


print(sum([1 for r in regions if fits(r)]))
