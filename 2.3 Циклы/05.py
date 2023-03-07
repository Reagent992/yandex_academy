summa = 0
while (f := float(input())) != 0:
    if f >= 500:
        f = f * 0.9
        summa += f
    else:
        summa += f
print(summa)
