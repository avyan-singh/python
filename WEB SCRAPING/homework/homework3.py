import requests
import bs4  
url=requests.get('https://quotes.toscrape.com/page/1/')
soup=bs4.BeautifulSoup(url.text,'lxml')
quotes=soup.select('.text')
quotes_texts = list(quote.text for quote in quotes)
print(quotes_texts)