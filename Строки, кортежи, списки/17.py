a = input()
c = a.lower()
b = c[::-1]
c = c.replace(' ', '')
b = b.replace(' ', '')
if c == b:
    print('YES')
else:
    print('NO')
