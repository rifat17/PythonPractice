from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "http://www.google.com"
filrpath = 'html/google.html'


class ScraperClass:
    __url       = ''
    __data      = ''
    __wlog      = None
    __soup      = None
    __filepath  = ''
    __dirPath = 'html/'

    def __init__(self, url, wlog):
        self.__url  = url
        self.__wlog = wlog

    def retriveWebpage(self):
        try:
            webHtml     = urlopen(self.__url)
        except Exception as e:
            print(e)
            self.__wlog.report(e)
        else:
            self.__data = webHtml.read()
            if len(self.__data) > 0 :
                print("Retrive Successfully")
                self.__wlog.report("Retrive Successfully")

    def writeWebpageAsHtml(self, fileName=filrpath, data=''):
        try:

            finalPath = self.__dirPath + fileName

            self.__filepath = finalPath

            with open(finalPath,'wb') as fObj:
                if data:
                    fObj.write(data)
                else:
                    fObj.write(self.__data)
        except Exception as e:
            print(e)
            self.__wlog.report(e)



    def printFilepath(self):
        print(self.__filepath)


    def readWebpageFromHtml(self, filepath=filrpath):
        try:
            with open(filepath) as fObj:
                self.__data = fObj.read()
        except Exception as e:
            print(e)
            self.__wlog.report(e)


    def changeUrl(self, url=''):
        if len(url) > 0:
            oldUrl      = self.__url
            self.__url  = url
            self.__wlog.report("Url changed to ", url , " from ", oldUrl)
        else:
            print("Error. No Url Provided.Not changed")
            self.__wlog.report("Error. No Url Provided.Not changed")

    def changeFilePath(self, fullPath=''):
        if fullPath:
            oldFilePath = self.__filepath
            self.__filepath = fullPath
            self.__wlog.report("filepaht changed to ", url , " from ", oldFilePath)
        else:
            print("Error. No filepath Provided.Not changed")
            self.__wlog.report("Error. No filepath Provided.Not changed")


    def convertDataToBS4(self):

        self.__soup = BeautifulSoup(self.__data, 'html.parser')

    def soupToSimpleHtml(self):
        # this mathod should update
        # should be able to take list of soup argument

        newsList = self.__soup.find_all(['div'])
        print(newsList)


    def printData(self):
        print(self.__data)
