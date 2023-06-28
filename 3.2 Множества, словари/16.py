# Зайка — 10
# Верно
words = []
answer = set()
while i := input().split():
    words += i

indexes = [i for i in range(len(words)) if words[i] == 'зайка']

for i in indexes:
    if i < len(words) - 1:
        answer.add(words[i + 1])
    if i != 0:
        answer.add(words[i - 1])

[print(i) for i in sorted(answer)]
