# Это будет шедевр!
# Верно.
ingredients = set()
recipes = dict()
[ingredients.add(input()) for i in range(int(input()))]
for i in range(int(input())):       # Число рецептов.
    dish = input()                  # Название блюда.
    for i2 in range(int(input())):  # Количество ингредиентов.
        if recipes.get(dish):
            recipes[dish].append(input())
        else:
            recipes[dish] = [input(), ]

answer = []
for i in recipes.items():           # Поиск подходящих блюд.
    f = set(i[1])
    if not f - ingredients:
        answer.append(i[0])

if answer:                          # Вывод отсортированных блюд.
    [print(i) for i in sorted(answer)]
else:
    print('Готовить нечего')
