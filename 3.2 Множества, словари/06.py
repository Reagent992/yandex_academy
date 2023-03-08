a = int(input())
b = int(input())
set_of_kids = list()

for i in range(a + b):
    set_of_kids.append(input())

set_of_kids2 = set_of_kids.copy()

for i2 in set_of_kids:
    if i2 in set_of_kids2:
        f = set_of_kids2.count(i2)
        if f > 1:
            for j in range(f):
                set_of_kids2.remove(i2)

f1 = sorted(set_of_kids2)
if f1:
    for i in f1:
        print(i)
else:
    print('Таких нет')
