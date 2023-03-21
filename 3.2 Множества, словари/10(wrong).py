# Транслитерация
# Ошибка на невидимом 3 тесте.
cyrillic_to_latin = {
    'А': 'A',
    'Б': 'B',
    'В': 'V',
    'Г': 'G',
    'Д': 'D',
    'Е': 'E',
    'Ё': 'E',
    'Ж': 'Zh',
    'З': 'Z',
    'И': 'I',
    'Й': 'I',
    'К': 'K',
    'Л': 'L',
    'М': 'M',
    'Н': 'N',
    'О': 'O',
    'П': 'P',
    'Р': 'R',
    'С': 'S',
    'Т': 'T',
    'У': 'U',
    'Ф': 'F',
    'Х': 'Kh',
    'Ц': 'Tc',
    'Ч': 'Ch',
    'Ш': 'Sh',
    'Щ': 'Shch',
    'Ы': 'Y',
    'Э': 'E',
    'Ю': 'Iu',
    'Я': 'Ia',
}

input_string = input()
list_string = list(input_string)

answer = []
for i in list_string:
    if i.islower():
        i = str(i).upper()
        if i in cyrillic_to_latin:
            letter = cyrillic_to_latin.get(i)
            answer.append(letter.lower())
    elif i.isupper():
        if i in cyrillic_to_latin:
            answer.append(cyrillic_to_latin.get(i))
    else:
        answer.append(i)

for i in answer:
    print(i, end='')
