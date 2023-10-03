"""
Разделяй и властвуй
https://new.contest.yandex.ru/41241/problem?id=149944/2022_10_21/zPScCZE950
Статус: Решено.
"""

input_file = input()
even_file = input()
odd_file = input()
eq_file = input()

array_of_digits = list()
even = ''  # Четные
odd = ''  # Нечертые
eq = ''

with open(input_file, 'r', encoding='UTF-8') as file_in:
    for line in file_in:
        for digit in line.rstrip('\n').split():
            even_amount = 0
            odds_amount = 0
            for number in map(int, list(digit)):
                if number % 2 == 0:
                    even_amount += 1
                elif number % 2 == 1:
                    odds_amount += 1
            if odds_amount > even_amount:
                odd += digit + ' '
            elif even_amount > odds_amount:
                even += digit + ' '
            elif odds_amount == even_amount:
                eq += digit + ' '
        odd += '\n'
        even += '\n'
        eq += '\n'

answer_dict = {
    even_file: even,
    odd_file: odd,
    eq_file: eq,
}

for file, string in answer_dict.items():
    with open(file, 'w', encoding='UTF-8') as file_out:
        file_out.write(string)
