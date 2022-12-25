c = []
while True:
    b = input()
    if not b:
        break
    if b.find('#') != -1:
        f = b.index('#')
        if f != 0:
            c.append(b[:f])
    else:
        c.append(b)

for g in range(len(c)):
    print(c[g])
