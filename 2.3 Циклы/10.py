x = 0
y = 0
a = input()
while a != 'СТОП':
    b = int(input())
    if a == 'СЕВЕР':
        x += b
    elif a == 'ЮГ':
        x -= b
    elif a == 'ЗАПАД':
        y -= b
    elif a == 'ВОСТОК':
        y += b
    a = input()

print(x)
print(y)
