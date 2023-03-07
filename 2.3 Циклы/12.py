a = int(input())
my_list = []

for i in str(a):
    my_list.append(int(i))

b = my_list[0]
# c = my_list[1]

for i in my_list:
    if b < i:
        b = i
print(b)
