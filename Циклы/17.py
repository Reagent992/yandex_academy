number = int(input())  # Получаем число
temp_list = []  # создаем пустой список для числа
for h in str(number):  # наполняем список цифрами из полученного числа
    temp_list.append(int(h))
temp_list2 = []  # создаем еще пустой список для числа
for f in temp_list:
    if f % 2 > 0:
        temp_list2.append(f)

print(''.join(map(str, temp_list2)))
