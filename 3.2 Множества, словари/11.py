# Однофамильцы
# Решено.

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
        num += i[1]

print(num)
