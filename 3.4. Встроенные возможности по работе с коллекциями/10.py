#  Мы делили апельсин 2.0
#  Верно.
from itertools import product

number = int(input())
print('А Б В')
f = range(1, number - 1)
################################

for i in (product(f, f, f)):
    if sum(i) == number:
        print(' '.join(map(str, i)))
