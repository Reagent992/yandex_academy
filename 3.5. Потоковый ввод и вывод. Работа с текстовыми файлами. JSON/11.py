"""
Файловая статистика 2.0
https://new.contest.yandex.ru/41241/problem?id=149944/2022_10_21/pQF9W4OE5J
Статус: Решено.
"""
import json

# TODO: пеменять ввод при отправке.
# input_txt_file_name = input()
# output_json_file_name = input()
input_txt_file_name = 'numbers.txt'
output_json_file_name = 'statistics.json'
numbers_array = list()

with open(input_txt_file_name, encoding="UTF-8") as file_in:
    for line in file_in:
        numbers_array.extend(line.strip('\n').split())

numbers_array = list(map(int, numbers_array))

len_of_numbers = len(numbers_array)
sum_numbers = sum(numbers_array)
positive_nums = [x for x in numbers_array if x > 0]

data = {
    "count": len_of_numbers,
    "positive_count": len(positive_nums),
    "min": min(numbers_array),
    "max": max(numbers_array),
    "sum": sum_numbers,
    "average": round(sum_numbers / len_of_numbers, 2),
}

with open(output_json_file_name, "w", encoding="UTF-8") as file_out:
    json.dump(data, file_out, ensure_ascii=False, indent=4)
