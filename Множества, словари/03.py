a = int(input())
b = set()
#  принимаем строки, делим на слова, добавляем с сетБ
while a != 0:
    c = input().split(' ')
    for i in c:
        b.add(i)
    a -= 1

for i in b:
    print(i)
