g = []
while True:
    text = input()
    if not text:
        break
    if text[0:2] == '##' and text[-3::1] != '@@@':
        g.append(text.strip('##'))
    if text[0:2] != '##' and text[-3::1] != '@@@':
        g.append(text)
    if text[-3::1] == '@@@':
        continue

for n in g:
    print(n)
