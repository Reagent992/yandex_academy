a = int(input())  # Будем делать "а" циклов

c = []  # ответ
for i in range(a):  # Запускаем ниженаписаное "а" раз.
    d = 0  # "Одноразовая" переменная

    number = int(input())  # Получаем число
    temp_list = []  # создаем пустой список для числа
    for h in str(number):  # наполняем список цифрами из полученного числа
        temp_list.append(int(h))
    for f in temp_list:  # Ищем наибольшее число и сохраняем его в d
        if f > d:
            d = f
    c.append(d)  # сохраняем цифру вне цикла

print(''.join(map(str, c)))
