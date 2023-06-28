#  Числовой прямоугольник 3.0
#  решить надо через itertools.product()
#  Не знаю как это решить "красиво"
from itertools import product

x = 2
y = 3
f = range(1, x * y + 1)

values = list(product(f, ' '), )
print(values)
"""
Есть список [(1,), (2,), (3,), (4,), (5,), (6,)]
как разделит его на x строчек?
"""

"""
Решение из интернета(в нем проблема с выводом):
Тут product определяет место для вывода цифры. 
Потенциально не решена проблема с пробелами при больших числах.

combinations = list(product(rows, columns))

counter = 1
for i, j in combinations:
    if j == 0 and i != 0:
        print()
    print(counter, end=' ')  # Нужно выравнять
    counter += 1
    
"""
