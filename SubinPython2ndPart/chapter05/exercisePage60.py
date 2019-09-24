import os

rootPath = os.getcwd()
# print('\n\n' + rootPath + '\n\n')
dirPath = os.path.join(rootPath, 'countryByLtr')
# print('\n\n' + dirPath + '\n\n')
if os.path.exists(dirPath):
    print(dirPath)
else:
    os.makedirs(dirPath)
try:
    with open('country.txt', 'r') as rf:
        for line in rf:
            # print(line)
            # print(line[0])
            fileName = line[0] + '.txt'
            # print(fileName)
            # print("/countryByLtr/"+fileName)
            finalPath = os.path.join(dirPath, fileName)
            with open(finalPath, 'a') as wf:
                wf.write(line)
except FileNotFoundError as e:
    print(e)
