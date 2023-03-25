# Транслитерация
# Верно(гпи сделал это короче(решить не смог))
translit_dict = {
    'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E', 'Ё': 'E',
    'Ж': 'Zh', 'З': 'Z',
    'И': 'I', 'Й': 'I', 'К': 'K', 'Л': 'L', 'М': 'M', 'Н': 'N', 'О': 'O',
    'П': 'P', 'Р': 'R',
    'С': 'S', 'Т': 'T', 'У': 'U', 'Ф': 'F', 'Х': 'Kh', 'Ц': 'Tc', 'Ч': 'Ch',
    'Ш': 'Sh', 'Щ': 'Shch',
    'Ы': 'Y', 'Э': 'E', 'Ю': 'Iu', 'Я': 'Ia', 'ь': '', 'Ь': '', 'Ъ': '',
    'ъ': ''
}

input_str = input()

for letter in input_str:
    if letter.upper() in translit_dict:
        print(translit_dict[letter.upper()].lower() if letter.islower() else
              translit_dict[letter.upper()], end='')
    else:
        print(letter, end='')
