# Множество всех полных квадратов
# Верно
numbers = [number for number in range(16, 100, 4)]
# [16, 20, 24, 28, 32, 36, 40, 44, 48,
# 52, 56, 60, 64, 68, 72, 76, 80, 84, 88, 92, 96]

print([x ** 0.5 for x in numbers])
f = [x for x in numbers if x ** 0.5 % 2 == 0 or x ** 0.5 % 2 == 1]
print(f)

numbers = [1, 2, 3, 4, 5]
print([x ** 0.5 for x in numbers])
f = [x for x in numbers if x ** 0.5 % 2 == 0 or x ** 0.5 % 2 == 1]
print(f)
print(16 // 1)
