# Кашееды — 4
# Решено
iterations = int(input())
dictionary = {}
# этот вариант не работает когда у одной фамилии две каши
for i in range(iterations):
    inpt = input().split(' ')
    last_name = inpt.pop(0)
    # print('Фамилия:', last_name)
    # print('Каши:', inpt)
    porridge = inpt
    for i2 in porridge:
        # print('1 Каша:', i2)
        if i2 not in dictionary:
            dictionary[i2] = last_name
        else:
            dictionary[i2] += ' ' + last_name
# print(dictionary)

porridge_output = input()
if porridge_output in dictionary:
    out = dictionary[porridge_output].split(' ')
    out.sort()
    for i in out:
        print(i)
else:
    print('Таких нет')
