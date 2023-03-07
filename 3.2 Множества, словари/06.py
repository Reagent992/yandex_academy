a = int(input())
b = int(input())
c = set()
d = set()

for i in range(a):
    c.add(input())

for i in range(b):
    d.add(input())

g = c.symmetric_difference(d)
g = list(g)
g = sorted(g)
if len(g) > 0:
    for i in g:
        print(i)
else:
    print('Таких нет')

