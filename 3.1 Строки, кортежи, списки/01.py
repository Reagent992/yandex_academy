b = ()
for i in range(int(input())):
    a = input()
    if (a[0] == 'а' or a[0] == 'б' or a[0] == 'в') and b != 0:
        b = 1
    else:
        b = 0
if b == 1:
    print('YES')
else:
    print('NO')
