n = int(input())
if n == 0 or n == 1:
    print('NO')
else:
    def IsPrime(n):
        d = 2
        while d * d <= n and n % d != 0:
            d += 1
        return d * d > n

    if IsPrime(n):
        print('YES')
    else:
        print('NO')
