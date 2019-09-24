import io

fileName = 'file.txt'

mode = 'r'

try:
    with open(fileName, mode) as fp:
        content = fp.read()
        print(content)
except FileNotFoundError:
    print(fileName, "not found. Please check if the file name is correnct")
except io.UnsupportedOperation:
    print("Are you sure", fileName, "is readable?")
