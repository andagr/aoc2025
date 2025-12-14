coords = [
    tuple([int(coord) for coord in line.split(",")])
    for line in open("input.txt", mode="r")
]

walls = [(coords[i], coords[(i + 1) % len(coords)]) for i in range(0, len(coords))]


def area(c1, c2):
    (x1, y1) = c1
    (x2, y2) = c2
    return (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)


def is_within(c1, c2):
    (x1, y1) = c1
    (x2, y2) = c2
    left = min(x1, x2)
    right = max(x1, x2)
    top = min(y1, y2)
    bottom = max(y1, y2)
    return not any(
        [
            (
                w_x1 == w_x2
                and w_x1 > left
                and w_x1 < right
                and not (max(w_y1, w_y2) <= top or min(w_y1, w_y2) >= bottom)
                or w_y1 > top
                and w_y1 < bottom
                and not (max(w_x1, w_x2) <= left or min(w_x1, w_x2) >= right)
            )
            for ((w_x1, w_y1), (w_x2, w_y2)) in walls
        ]
    )


print(
    max(
        [
            area((x1, y1), (x2, y2))
            for (x2, y2) in coords
            for (x1, y1) in coords
            if x2 != x1 and y2 != y1 and is_within((x1, y1), (x2, y2))
        ]
    )
)
