# Дайте чего-нибудь новенького!
# Верно.
today_menu = set()
weeks_menu = set()
[today_menu.add(input()) for i in range(int(input()))]
[weeks_menu.add(input()) for i2 in range(int(input())) for i3 in
 range(int(input()))]

dif = today_menu - weeks_menu
if dif:
    [print(i) for i in sorted(dif)]
else:
    print('Готовить нечего')
