import requests
import sys

imgUrl = sys.argv[1]
fileNmae = sys.argv[2]

r = requests.get(imgUrl)

with open(fileNmae, 'wb') as f:
    f.write(r.content)
