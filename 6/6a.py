from math import prod

lines = [line.strip() for line in open("input.txt", "r")]

operators = [op for op in lines[len(lines) - 1].split()]
numbers = list(zip(*[[int(n) for n in lines[y].split()] for y in range(0, len(lines) - 1)]))

def operate(operator, numbers):
    if operator == '+': return sum(numbers)
    else: return prod(numbers)

print(sum([operate(operators[i], numbers[i]) for i in range(0, len(operators))]))