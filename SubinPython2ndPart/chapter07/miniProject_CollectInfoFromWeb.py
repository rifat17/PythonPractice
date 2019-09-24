import re
import requests
import sys
import os


def create_directory(name):
	print("Creating Directory..",name)
	try:
		os.mkdir(name)
	except Exception as e:
		# raise e
		print(name, "already exists")

def downloadImage(imgUrl, fileName):
	print("Downloading..",imgUrl)
	r = requests.get(imgUrl)

	with open(fileName,'wb') as f:
		f.write(r.content)

def getDirectory(regex, url):
	result 	= re.findall(regex,url)
	dirName = "_".join(result[0])
	return dirName

def process():
	# Creating home Directory
	mainDir 	= "dimik_pub"
	create_directory(mainDir)

	url 		= "http://dimik.pub"

	response 	= requests.get(url)

	if response.ok is False:
		sys.exit("Could not get response from server")

	pageContent = response.text

	regexp 		= re.compile(r'<div class="book-cover">\s*<a href="(.*?)">\s+<img src="(.*?)">\s+[a-z</>\s\.\w!-=]+<h2 class="sd-title">\s+<a href="(.*?)">(.*?)</a>')
	#																0					1															2		3
	result		= re.findall(regexp, pageContent)

	dirRegex 	= re.compile(r'(book)/(\d+)/(.+)\w+')

	for item in result:
		itemName 	= item[3]
		itemUrl		= item[0]
		itemImgUrl	= item[1]

		dirName 	= mainDir + "/" + getDirectory(dirRegex, itemUrl)
		create_directory(dirName)

		fileName	= dirName + "/" + "info.txt"
		with open(fileName, "w") as fp:
			fp.write(itemName + "\n")
			fp.write(itemUrl)

		imgFileName	= dirName + "/" + "image.png"
		downloadImage(itemImgUrl, imgFileName)


if __name__ == "__main__":
	process() 




# [<a-z ="]+footer-col-\d[.\s\w<>="-]+>(.+?)+\s+(<a href="(.+)">(.*?)</a>\s+)+
# [<a-z ="]+footer-col-\d[.\s\w<>="-]+>(.+?)+\s+(<a href="(.+)">(.+?\s*.+?)</a>\s+)+
