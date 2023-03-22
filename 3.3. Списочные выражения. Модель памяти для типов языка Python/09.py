# Преобразование в строку
# Верно.
numbers = [3, 1, 2, 3, 2, 2, 1]
numbers2 = [1, 1, 3, 1, 10, 2, 4, 6, 7, 1, 2, 7]

f = ' - '.join([str(x) for x in sorted(set(numbers2))])
print(f)
