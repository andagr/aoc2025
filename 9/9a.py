coords = [tuple([int(coord) for coord in line.split(",")]) for line in open("input.txt", mode="r")]

def area(c1, c2):
    (x1, y1) = c1
    (x2, y2) = c2
    return (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)

print(max([area(c1, c2) for c2 in coords for c1 in coords]))
