a = int(input())
b = int(input())
c = []
for i in range(a, b + 1):
    c.append(i)
print(" ".join(map(str, c)))
