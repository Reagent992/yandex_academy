# Найдётся всё 2.0
# Верно.
from sys import stdin

lines = list()

for line in stdin:
    string = line.rstrip("\n")
    lines.append(string)

query = lines.pop()
[print(i) for i in lines if query in str(i.lower())]
