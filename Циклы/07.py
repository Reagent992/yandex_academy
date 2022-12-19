a = int(input())
b = int(input())
at = a
bt = b
if a != b:
    while a != b:
        if b > a:
            a += at
        else:
            b += bt
print(a)
