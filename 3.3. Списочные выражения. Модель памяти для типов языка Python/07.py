# Делители
# Верно
numbers = {1, 2, 3, 4, 5}
numbers2 = {15, 49, 36}
f = {x: [f for f in range(1, x + 1) if x % f == 0] for x in sorted(numbers)}
print(f)
