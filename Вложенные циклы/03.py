a = int(input())  # Получаем стартовое значение
b = 0  # Переменная для ограничения рядов и строк
e = 0  # изменяемое кол-во рядов
# Выводим меняющееся значение "i от a" b раз, после переходим на новую строку и продолжаем с b + 1.
# Первый перебор
for i in range(a):  # запускаем написанное внутри 'а' раз.
    print(i + 1, end=' ')  # выводим текущее "и" в строку
    if e == b:  # проверяем кол-во рядов
        e = 0   # сбрасываем кол-во рядов
        b += 1  # увеличиваем кол-во рядом и строк
        print()  # переходим на следующую строку
        continue  # переходим к следующей итерации без выполнения ниже написанного
    e += 1  # считаем кол-во рядов которых вывели
