from sys import stdin

lines = []
for line in stdin:
    string = line.rstrip("\n")

    if '#' in string:
        start = string.index('#')
        if start > 0 and start != 0:
            lines.append(string[0:start])

    else:
        lines.append(string)

for i in lines:
    print(i)
