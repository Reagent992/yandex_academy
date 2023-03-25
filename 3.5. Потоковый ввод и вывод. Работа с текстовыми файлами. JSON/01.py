from sys import stdin

lines = []
for line in stdin:
    lines += line.rstrip("\n").split()
answr = 0
for i in lines:
    answr += int(i)
print(answr)
