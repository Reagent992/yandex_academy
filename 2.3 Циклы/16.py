def test(a):
    a = list(str(a))
    b = a[::-1]
    if a == b:
        print('YES')
    else:
        print('NO')

test(123454321)