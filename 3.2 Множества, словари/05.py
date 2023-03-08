a = int(input())
b = int(input())
c = []
d = 0
f = []

for i in range(a + b):
    c.append(input())

for i in c:
    if i not in f:
        f.append(i)
        d += 1
    else:
        d -= 1


if d != 0:
    print(d)

else:
    print('Таких нет')
