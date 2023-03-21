# Аббревиатура
# Верно
string = 'Российская Федерация'

f = ''.join([x[0].upper() for x in string.split(' ')])
print(f)
