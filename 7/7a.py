lines = lines = [line.strip("\n") for line in open("input.txt", "r")]

matrix = [list(l) for l in lines]

for row in range(1, len(matrix)):
    for col in range(0, len(matrix[row])):
        if matrix[row - 1][col] == "S":
            matrix[row][col] = "|"
        elif matrix[row - 1][col] == "|":
            if matrix[row][col] == "^":
                matrix[row][col - 1] = "|"
                matrix[row][col + 1] = "|"
            else:
                matrix[row][col] = "|"
print(
    sum(
        [
            1
            for row in range(0, len(matrix))
            for col in range(0, len(matrix[row]))
            if matrix[row - 1][col] == "|" and matrix[row][col] == "^"
        ]
    )
)
