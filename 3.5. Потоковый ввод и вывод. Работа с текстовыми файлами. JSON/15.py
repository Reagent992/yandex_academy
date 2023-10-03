"""
Поставь себя на моё место
https://new.contest.yandex.ru/41241/problem?id=149944/2022_10_21/zcXhJfSSBM
Статус: Решено.
"""

import json
from sys import stdin

# Ввод данных.
user_input = [line.strip() for line in stdin]
user_input.reverse()


# TODO: Заменить перед отправкой.
# user_input = ['4', '12', '3', '100', '0']
# user_input.reverse()


def read_json_file() -> list:
    """Чтенеие ответов из файла."""
    with open('scoring.json', encoding="UTF-8") as file_in:
        return json.load(file_in)


def get_anser_to_point_dict(data_dict) -> list:
    """Создание словаря ответ: очки."""
    answer = list()
    for data in data_dict:
        points: int = data['points']
        tests_len: int = len(data['tests'])
        test_value = points // tests_len
        answer.append({test['pattern']: test_value for test in data['tests']})
    return answer


def main() -> int:
    answer = 0
    for i in get_anser_to_point_dict(read_json_file()):
        for key, value in i.items():
            if key == user_input.pop():
                answer += value
    return answer


if __name__ == '__main__':
    print(main())
