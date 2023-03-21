# Буквенная статистика
# Решено
text = 'Мама мыла раму!'

a = {x: [x for x in list(sorted(text.lower())) if x.isalpha()].count(x)
     for x in [x for x in list(sorted(text.lower())) if x.isalpha()]}
print(a)

# Лучше:
f = {x: text.lower().count(x) for x in list(sorted(text.lower())) if x.isalpha()}
print(f)
