"""
# Транслитерация 2.0
https://new.contest.yandex.ru/41241/problem?id=149944/2022_10_21/9aq4Sr8kim
Статус: Верно.
"""

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

lines = []

with open("numbers.txt", encoding="UTF-8") as file_in:
    for line in file_in:
        lines.append(line)

lines = [list(x) for x in lines]

answer = list()
for lines in lines:
    for letter in lines:
        if letter.upper() in translit_dict:
            answer.append(
                translit_dict[letter.upper()].lower() if letter.islower() else
                translit_dict[letter.upper()])
        else:
            answer.append(letter)

with open("second.txt", "w", encoding="UTF-8") as file_out:
    file_out.writelines(''.join(answer))
