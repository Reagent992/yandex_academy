# Однофамильцы
# Ошибка на 6 тесте.

a = int(input())

dictionary = {}

for i in range(a):
    intp = input()
    if intp in dictionary:
        dictionary[intp] += 1
    else:
        dictionary[intp] = 1

num = 0
for i in dictionary.items():
    if i[1] > 1:
        num += 1
        print(i[0], '-', i[1])

if num == 0:
    print('Однофамильцев нет')
