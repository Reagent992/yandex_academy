#  я забил на это
a = int(input())  # кол-во строк
b = int(input())  # кол-во рядов
h = ' '  # разделитель
c = 1
for i in range(a):  # строки
    c = i + 1
    for g in range(b):  # ряды
        if g % 2 == 0:
            n = len(str(c))  # разрядность выводимого числа
            j = len(str(a * b))  # разрядность финального числа
            ff = j - n  # разница в разрядности текущего и финального
            if n < j:  # добавление пробелов
                print(h * ff, end='')
            print(c, end=' ')
            c += (a * 2) - (i + 2)

        else:
            n = len(str(c))  # разрядность выводимого числа
            j = len(str(a * b))  # разрядность финального числа
            ff = j - n  # разница в разрядности текущего и финального
            if n < j:  # добавление пробелов
                print(h * ff, end='')
            print(c, end=' ')
            c += 1
    print()
