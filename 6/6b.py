from math import prod

lines = [[x.replace("\n", " ") for x in line] for line in open("input.txt", "r")]

def operate(operator, numbers):
    if operator == "+": return sum(numbers)
    else: return prod(numbers)

op = ""
nums = []
results = []
for x in range(0, len(lines[0])):
    col = [lines[y][x] for y in range(0, len(lines))]
    if col[len(col) - 1] == "*":
        op = "*"
    elif col[len(col) - 1] == "+":
        op = "+"

    if all([s == " " for s in col]):
        results.append(operate(op, nums))
        op = ""
        nums.clear()
    else:
        nums.append(int("".join(col[:-1])))

print(sum(results))