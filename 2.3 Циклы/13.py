a = int(input())
win = 'я'
while a != 0:
    b = input()
    if win > b:
        win = b

    a -= 1
print(win)
