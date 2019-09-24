from webscrap import wlog
from webscrap import wscrap

wlog.setCustomLogInfo('html/error.log')

url = "http://127.0.0.1:8000/Downloads/How%20to%20scrape%20websites%20with%20Python%20and%20BeautifulSoup.html"


testScrap = wscrap.ScraperClass(url, wlog)
testScrap.retriveWebpage()
testScrap.writeWebpageAsHtml()

testScrap.readWebpageFromHtml()
testScrap.printData()
testScrap.printFilepath()
