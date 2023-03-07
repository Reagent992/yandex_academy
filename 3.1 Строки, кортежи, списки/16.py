a = int(input())  # длинна заголовка
b = int(input())  # кол-во строк в заголовке новости
g = []  # хранение

for i in range(b):
    g.append(input())  # сохраняем заголовок
c = len(''.join(g))

if c > a:
    a -= 3
    for i in g:
        if len(i) < a:
            if len(i[0:a]) >= 0:
                print(i[0:a])
                a -= len(i)
        else:
            if a > 0:
                print(i[0:a], end='...')
                a -= len(i)
else:
    print(g)
