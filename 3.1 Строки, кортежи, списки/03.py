a = int(input())
b = int(input())
g = []
for i in range(b):
    c = input()
    if len(c) > a:
        g.append(f'{c[0:a-3]}...')
    else:
        g.append(c)
for n in g:
    print(n)
