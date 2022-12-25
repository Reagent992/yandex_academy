a = int(input())
c = []
for i in range(a):
    b = input()
    c.append(b.find('зайка') + 1)

for g in range(len(c)):
    if c[g] != 0:
        print(c[g])
    else:
        print('Заек нет =(')
