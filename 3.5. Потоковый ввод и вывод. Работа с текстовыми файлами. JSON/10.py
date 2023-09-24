"""
Хвост
https://new.contest.yandex.ru/41241/problem?id=149944/2022_10_21/fLdP3vEf3r
Статус: Решено.
"""
# file_name = input()
# last_lines = int(input())
file_name = 'numbers.txt'
last_lines = 2
words = list()

with open(file_name) as read_file:
    for line in read_file:
        words.append(line.rstrip('\n'))

print('\n'.join(words[-last_lines:]))
