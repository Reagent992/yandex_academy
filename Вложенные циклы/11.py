g = 0
for i in range(int(input())):
    n = int(input())
    if n == 0 or n == 1:
        continue
    else:
        def IsPrime(n):
            d = 2
            while d * d <= n and n % d != 0:
                d += 1
            return d * d > n

        if IsPrime(n):
            g += 1

print(g)
