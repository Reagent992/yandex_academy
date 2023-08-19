"""
Файловая статистика
https://new.contest.yandex.ru/41241/problem?id=149944/2022_10_21/vnXf89aHT3
Статус: Верно.
"""

all_numbers = list()

file_name = input()

with open(file_name, encoding="UTF-8") as file_in:
    for line in file_in:
        all_numbers.extend(line.strip('\n').split())

all_numbers = list(map(int, all_numbers))

len_of_numbers = len(all_numbers)
sum_numbers = sum(all_numbers)
positive_nums = [x for x in all_numbers if x > 0]
print(all_numbers)
print(len_of_numbers)
print(len(positive_nums))
print(min(all_numbers))
print(max(all_numbers))
print(sum_numbers)
print(round(sum_numbers / len_of_numbers, 2))
