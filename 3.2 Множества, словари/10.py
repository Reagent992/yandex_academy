# Транслитерация
# Верно.
dict = {
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
    'ь': '',
    'Ь': '',
    'Ъ': '',
    'ъ': '',
}

for letter in list(input()):

    if letter.islower():
        letter2 = letter.upper()
        if letter2 in dict:
            print(dict.get(letter2).lower(), end='')

        else:
            print(letter, end='')

    elif letter.isupper():
        if letter in dict:
            print(dict.get(letter), end='')

        else:
            print(letter, end='')

    else:
        print(letter, end='')
