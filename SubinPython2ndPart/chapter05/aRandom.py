import random
# print(dir(random))
capitalLtrList = []
smallLtrList = []

for i in range(0, 26):
    capitalLtrList.append(chr(65+i))
    smallLtrList.append(chr(97+i))

# for i in ltrList:
#     print(i)
country = []
# for i in capitalLtrList:
#     country.append(i)

# print(country[5])
aStr = ''
for i in range(1, 200):
    firstLtr = random.randint(0, 25)
    aRandomNumber1 = random.randint(0, 25)
    aRandomNumber2 = random.randint(0, 25)
    aRandomNumber3 = random.randint(0, 25)
    aRandomNumber4 = random.randint(0, 25)
    aRandomNumber5 = random.randint(0, 25)
    # print(aRandomNumber)
    # print(smallLtrList[aRandomNumber])
    aStr = capitalLtrList[firstLtr] + smallLtrList[aRandomNumber1] + \
        smallLtrList[aRandomNumber2] + smallLtrList[aRandomNumber3] + \
        smallLtrList[aRandomNumber4] + smallLtrList[aRandomNumber5]
    # print(aStr)
# could be done with
    # aStr = ''.join((capitalLtrList[firstLtr], smallLtrList[aRandomNumber1]))
    # print(aStr)

    country.append(aStr)
country.sort()
# print(country)

with open('country.txt', 'w', encoding='utf-8') as f:
    for aCountry in country:
        f.write(aCountry+'\n')
