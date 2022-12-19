a = int(input())
b = int(input())
c = []
if b > a:
    for i in range(a, b + 1):
        c.append(i)
    print(" ".join(map(str, c)))
elif a > b:
    for i in range(a, b - 1, -1):
        c.append(i)
    print(" ".join(map(str, c)))
elif a == b:
    print(a)
