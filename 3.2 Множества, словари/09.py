# Зайка — 9
# Решено.

dictionary = {}

while a := input():
    split_a = a.split(' ')
    for i in split_a:
        if i in dictionary:
            dictionary[i] += 1
        else:
            dictionary[i] = 1

for i2 in dictionary.items():
    print(i2[0], i2[1])
