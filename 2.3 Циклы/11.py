a = int(input())
res = [int(x) for x in str(a)]
ans = 0
for i in res:
    ans += i
print(ans)
