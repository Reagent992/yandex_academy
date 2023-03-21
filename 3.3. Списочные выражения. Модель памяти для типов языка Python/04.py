# Множество нечетных чисел
# Верно
numbers = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2]
f = set([x for x in numbers if x % 2 != 0])
print(f)
