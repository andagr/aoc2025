lines = []
with open('input.txt', 'r') as file:
    lines = [line.strip() for line in file]

zeroCount = 0
sum = 50
for line in lines:
    value = int(line[1:])
    if line.startswith('L'):
        sum = (sum - value) % 100
    elif line.startswith('R'):
        sum = (sum + value) % 100
    if sum == 0:
        zeroCount += 1

print(zeroCount)

