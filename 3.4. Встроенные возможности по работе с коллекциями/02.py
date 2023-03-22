# Сборы на прогулку
# Верно
a = 'Аня, Вова'
b = 'Боря, Дима, Гена'

f = list(zip(a.split(', '), b.split(', ')))
for i in f:
    print(i[0], '-', i[1])

