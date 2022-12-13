#  Задача:
"""Легенды велогонок возвращаются: кто быстрее? В новом сезоне за первенство в велогонках вновь борются лучшие из
лучших. Протяжённость заключительной трассы — 43872м, и все хотят знать, кто получит золотую медаль.

Нам известны средние скорости трёх претендентов на победу – Пети, Васи и Толи. Кто из них победит?

Формат ввода
В первой строке записана средняя скорость Пети.
Во второй — Васи.
В третьей — Толи.

Формат вывода
Красивый пьедестал (ширина ступеней 8 символов).

Примечание
В данный момент визуализация тестов работает некорректно.
Ответ на первый тест:

          Петя
  Толя
                  Вася
   II      I      III
Пример 1
Ввод
10
5
7
Вывод
          Петя
  Толя
                  Вася
   II      I      III
Пример 2
Ввод
5
7
10
Вывод
          Толя
  Вася
                  Петя
   II      I      III
"""

#  получаем вводные:
s = 43872
p = int(input())
v = int(input())
t = int(input())
# Определяем первое место
if v < p < t or p < v < t:
    p1 = 'Толя'
elif p < t < v or t < p < v:
    p1 = 'Вася'
else:
    p1 = 'Петя'
# второе
if v < p < t or t < p < v:
    p2 = 'Петя'
elif p < v < t or t < v < p:
    p2 = 'Вася'
else:
    p2 = 'Толя'
# третье
if p < v < t or p < t < v:
    p3 = 'Петя'
elif v < p < t or v < t < p:
    p3 = 'Вася'
else:
    p3 = 'Толя'
print(f'          {p1}          ')
print(f'  {p2}  ')
print(f'                  {p3}  ')
print(f'   II      I      III   ')
