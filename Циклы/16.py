# получаем число
a = int(input())
# делаем из него list
my_list = []
for i in str(a):
    my_list.append(int(i))
my_list2 = my_list.copy()
my_list3 = my_list.copy()
# узнаем длину половины списка
print(len(my_list))
g = len(my_list) % 2
b = round(len(my_list) / 2) - g
d = round(len(my_list) / 2) - g - 1
if g != 0:
    my_list3.pop(b)
f = len(my_list) - 1
h = b
j = d
# делаем первую половину списка
while h <= f:
    my_list2.pop(b)
    h += 1
# делаем вторую половину списка
while d >= 0:
    my_list3.pop(d)
    d -= 1
# переворачиваем вторую половину списка
my_list3.reverse()
# проверяем на одинаковость
if my_list2 == my_list3:
    print('YES')
else:
    print("NO")
