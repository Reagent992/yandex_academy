# Двоичная статистика!
# Верно, но двоичный код я считал не сам.
answer = []

bin_numbers_list = [bin(int(i))[2:] for i in input().split()]

for i in bin_numbers_list:
    i = [int(d) for d in i]
    answer.append({"digits": len(i),
                   "units": i.count(1),
                   "zeros": i.count(0)}
                  )

print(answer)
