aLine = "This is a line\n"

with open('text.txt', 'w+', encoding='utf-8') as f:
    for i in range(1, 10):
        f.write(str(i) + ' ' + aLine)
