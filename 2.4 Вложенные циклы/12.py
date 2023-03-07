a = int(input())  # кол-во строк
b = int(input())  # кол-во рядов
h = ' '
c = 1  # считаем и выводим
for i in range(a):  # строки
    for g in range(b):  # ряды
        n = len(str(c))  # разрядность выводимого числа
        j = len(str(a * b))  # разрядность финального числа
        ff = j - n  # разница в разрядности текущего и финального
        if n < j:  # добавление пробелов
            print(h * ff, end='')
        print(c, end=' ')
        c += 1
    print()
