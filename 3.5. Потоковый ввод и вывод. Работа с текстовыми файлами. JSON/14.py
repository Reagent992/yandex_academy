"""
Слияние данных
https://new.contest.yandex.ru/41241/problem?id=149944/2022_10_21/NglSlWUjFS
Статус: Решено.
"""
import json

users_json = input()
updates_json = input()
result = dict()

with open(users_json, encoding="UTF-8") as file_in:
    users = json.load(file_in)
with open(updates_json, encoding="UTF-8") as file_in:
    users_update = json.load(file_in)


def find_person(name, users_update):
    """Поиск человека в словаре по имени."""
    for person in users_update:
        if person.get('name') == name:
            person.pop('name')
            return person


for person in users:
    name = person.pop('name')
    person_update = find_person(name, users_update)
    if person_update:
        for key, value in person_update.items():
            if key in person:
                if person[key] < value:
                    person[key] = value
            else:
                person[key] = value
    result[name] = person

with open(users_json, "w", encoding="UTF-8") as file_out:
    json.dump(result, file_out, ensure_ascii=False, indent=4)
