# Автоматизация списка
# Верно.
a = 'картина корзина картонка'
for index, value in enumerate(a.split(' '), 1):
    print(f'{index}. {value}')
