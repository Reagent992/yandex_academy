# Рациональная считалочка
# Верно
from itertools import count

a, b, c = input().split(' ')


for value in count(float(a), float(c)):
    if value <= float(b):
        print("{:.2f}".format(value))
    else:
        break
