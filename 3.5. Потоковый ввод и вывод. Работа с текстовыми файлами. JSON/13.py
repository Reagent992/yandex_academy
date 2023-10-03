"""
Обновление данных
https://new.contest.yandex.ru/41241/problem?id=149944/2022_10_21/KY7DBzCEBP
Статус: Решено.

Логика:
- Читаем пользовательский ввод.
- Читаем JSON, записываем в словарь.
- Обновляем словарь значениями пользователя.
- Записываем новый JSON.
"""
import json
from sys import stdin

user_input = {}
json_file = input()
for line in stdin:
    clear_line = line.rstrip('\n').split(' == ')
    user_input[clear_line[0]] = clear_line[1]

with open(json_file, encoding="UTF-8") as file_in:
    json_data = json.load(file_in)

with open(json_file, "w", encoding="UTF-8") as file_out:
    json.dump(json_data | user_input, file_out, ensure_ascii=False, indent=4)
