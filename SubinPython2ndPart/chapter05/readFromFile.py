with open('text.txt', 'r') as f:
    content = f.read()
    print(content)

print(len(content))

with open('text.txt', 'r') as f:
    # lines = f.readlines()
    line = f.readline()  # single line only
print(line)


with open('text.txt', 'r') as f:
    for line in f:
        print(line)
