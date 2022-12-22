a = int(input())  # кол-во строк
b = int(input())  # кол-во рядов
h = ' '
c = 1  # считаем и выводим
for i in range(a):  # строки
    for g in range(b):  # ряды
        n = len(str(c))
        j = len(str(a * b))
        ff = j - n
        if n < j:
            print(h * ff, end='')
        print(c, end=' ')
        c += 1
    print()
