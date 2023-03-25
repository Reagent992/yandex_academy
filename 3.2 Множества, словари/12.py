# Однофамильцы
# Решено.

a = int(input())

last_names = dict()

for i in range(a):
    string = input()
    if string in last_names:
        last_names[string] += 1
    else:
        last_names[string] = 1

num = 0
answer = list()
for i in last_names.items():
    if i[1] > 1:
        num += 1
        answer.append(f'{i[0]} - {i[1]}')

if num == 0:
    print('Однофамильцев нет')
else:
    for i in sorted(answer):
        print(i)
