lines = [line.strip("\n") for line in open("input.txt", "r")]
matrix = [list(l) for l in lines]

cache = dict()


def step_cached(col, row=2):
    if row >= len(matrix):
        return 1

    if matrix[row][col] == ".":
        timelines = cache.get((row, col))
        if not timelines:
            timelines = step_cached(col, row + 1)
            cache[(row, col)] = timelines
        return timelines
    elif matrix[row][col] == "^":
        timelines = cache.get((row, col))
        if not timelines:
            timelines_left = step_cached(col - 1, row + 1)
            timelines_right = step_cached(col + 1, row + 1)
            timelines = timelines_left + timelines_right
            cache[(row, col)] = timelines
        return timelines


s = matrix[0].index("S")
print(step_cached(s))
