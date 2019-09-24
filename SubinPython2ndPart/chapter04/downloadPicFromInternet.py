import os
import requests
import webbrowser as wb

imgUrl = 'http://127.0.0.1:8000/pic/image1.jpeg'

r = requests.get(imgUrl)
# print(r.headers['Content-type'])
# print(r.headers['Content-type'].split('/')[0])
# print(r.headers['Content-type'].split('/')[1])
dirPath = os.path.join(os.getcwd(), 'Download/Picture')


# if os.path.exists()
# print(dirPath)

# if os.path.exists(dirPath):
#     print(dirPath)
#     print(os.makedirs(dirPath))
# else:
#     print("Path Does not Exit,Creating..")
#     print(os.makedirs(dirPath))
fileNmae = os.path.join(dirPath, 'image0001.jpg')
print(fileNmae)


if r.headers['Content-type'] == 'image/jpeg' and not os.path.exists(fileNmae):
    try:
        print(os.makedirs(dirPath))
    except FileExistsError as e:
        # print('Error : ', e)
        pass

    with open(fileNmae, 'wb') as imgf:
        print('saving..', fileNmae)
        imgf.write(r.content)

# wb.open("file://"+fileNmae)
wb.open('file:///home/hasib/PythonProjectFolder/SubinPython2ndPart/chapter04/Download/Picture/image0001.jpg')
