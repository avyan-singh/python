import requests
import bs4  
url=requests.get('https://quotes.toscrape.com/page/1/')
soup=bs4.BeautifulSoup(url.text,'lxml')
authors=soup.select('.author')
author_names = sorted(set(author.text for author in authors))
print(author_names)