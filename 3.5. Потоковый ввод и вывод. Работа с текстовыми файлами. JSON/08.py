"""
Файловая разница
https://new.contest.yandex.ru/41241/problem?id=149944/2022_10_21/jwbbCc9DZY
Статус: Решено.
"""
words_dict = dict()
# инпуты в тренажер
# first_file = input()
# second_file = input()
# answer_file = input()
# тестовые файлы
first_file = 'numbers.txt'
second_file = 'second.txt'
answer_file = 'answer.txt'
first_file_words = set()
second_file_words = set()

with open(first_file, encoding="UTF-8") as file_in:
    for line in file_in:
        [first_file_words.add(word) for word in
         line.rstrip('\n').split()]

with open(second_file, encoding="UTF-8") as file_in:
    for line in file_in:
        [second_file_words.add(word) for word in
         line.rstrip('\n').split()]

list_of_single_words = first_file_words ^ second_file_words


with open(answer_file, 'w', encoding="UTF-8") as file_out:
    file_out.writelines('\n'.join(sorted(list_of_single_words)))
