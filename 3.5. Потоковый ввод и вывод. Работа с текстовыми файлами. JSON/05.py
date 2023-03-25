# А роза упала на лапу Азора 6.0
# Верно.
from sys import stdin

lines = list()
answer = set()

for line in stdin:
    string = line.strip().split()
    [lines.append(i) for i in string]

[answer.add(i) for i in lines if i.lower()[::-1] == i.lower()]
[print(i) for i in sorted(answer)]
