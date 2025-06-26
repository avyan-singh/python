import requests
import bs4  
url=requests.get('https://quotes.toscrape.com/page/1/')
soup=bs4.BeautifulSoup(url.text,'lxml')
tags=soup.select('.tag-item')
tag_texts = list(quote.text for quote in tags)
for tag in tag_texts:
    print(tag)