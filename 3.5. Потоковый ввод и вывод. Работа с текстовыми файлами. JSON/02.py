from sys import stdin

lines = []
amount = 0
summa = 0
for line in stdin:
    inptt = line.rstrip("\n").split()
    lines.append(int(inptt[2]) - int(inptt[1]))
    amount += 1

for i in lines:
    summa += i

print(round(summa / amount))
