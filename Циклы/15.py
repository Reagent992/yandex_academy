a = int(input())
ans = 0
while a != 0:
    f = input()
    for i in f.split(' '):
        if i == 'зайка':
            ans += 1
    a -= 1
print(ans)
