lines = []
with open('input.txt', 'r') as file:
    lines = [line.strip() for line in file]

changes = (-int(line[1:]) if line[0] == 'L' else int(line[1:]) for line in lines)

zeroCount = 0
curr = 50
for change in changes:
    result = curr + change
    prev = curr
    curr = result % 100
    if change > 0 and result >= 100:
        zeroCount += result // 100
    elif change < 0 and result <= 0 and result > -100 and prev != 0:
        zeroCount += 1
    elif change < 0 and result <= -100 and prev == 0:
        zeroCount += -result // 100
    elif change < 0 and result <= -100 and prev > 0:
        zeroCount += (-result // 100) + 1

print(zeroCount)
