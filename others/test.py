from moduloTest import scraper
url = "http://127.0.0.1:8000/Downloads/How%20to%20scrape%20websites%20with%20Python%20and%20BeautifulSoup.html"
fileName = "webscrapingwithpythonTest.html"

scraper.getHtml(url=url,fileName=fileName)
