from itertools import accumulate

a = input().split()
for value in accumulate(a):
    print(value)
