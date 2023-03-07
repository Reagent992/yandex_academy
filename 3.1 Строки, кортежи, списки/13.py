a = int(input())  # Столько будет вводов в цикле
b = []  # храним вводы из цикла
for i in range(a):  #
    b.append(int(input()))
c = int(input())  # степень
for i in b:  # выводим ответ, возводим в степень список поочередно.
    print(i ** c)
