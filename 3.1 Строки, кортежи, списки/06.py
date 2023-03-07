a = int(input())
c = 0
for i in range(a):
    b = input().split()
    for h in b:
        if h == 'зайка':
            c += 1
print(c)
