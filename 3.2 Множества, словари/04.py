a = int(input())
b = int(input())
c = set()
d = set()
#  сохраняем инпут в сетС
while a != 0:
    e = input()
    c.add(e)
    a -= 1
#  сохраняем инпут в сетД
while b != 0:
    f = input()
    d.add(f)
    b -= 1
#  ищем общее и выводим
g = c & d
if len(g) > 0:
    print(len(g))
else:
    print('Таких нет')

