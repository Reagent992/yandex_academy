"""
Файловая чистка
https://new.contest.yandex.ru/41241/problem?id=149944/2022_10_21/RRiQ2NBHyc
Статус: Решено, но это ужасный код.
"""
# first_file = input()
# second_file = input()
first_file = 'numbers.txt'
second_file = 'second.txt'
result = list()
restricted = {'\n', '\t'}

with open(first_file, encoding="UTF-8") as file_in:
    for line in file_in:
        line = line.strip().rstrip('\n')
        clear_line = ''
        counter = 0
        while counter < len(line):
            if line[counter] in restricted:
                counter += 1
                continue
            clear_line += line[counter]
            counter += 1
        result.append(clear_line)

with open(second_file, 'w', encoding="UTF-8") as file_out:
    for line in result:
        if line:
            t = ' '.join(line.split())
            file_out.write(t + '\n')

