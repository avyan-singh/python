import requests
import bs4  
url=requests.get('https://quotes.toscrape.com/page/1/')
soup=bs4.BeautifulSoup(url.text,'lxml')
print(soup)