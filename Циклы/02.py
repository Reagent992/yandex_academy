a = 0
while (f := input()) != 'Приехали!':
    for i in f.split(' '):
        if i == 'зайка':
            a += 1
print(a)
