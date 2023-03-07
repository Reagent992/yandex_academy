a = ['Манная', 'Гречневая', 'Пшённая', 'Овсяная', 'Рисовая']
b = int(input())
d = b // len(a)
c = b % len(a)

for i in a * d:
    print(i)

for i in a[:c]:
    print(i)
