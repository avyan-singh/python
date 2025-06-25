import bs4
import requests
request=requests.get('https://en.wikipedia.org/wiki/Portugal')
soup=bs4.BeautifulSoup(request.text,'lxml')
# print(soup)
select=soup.select('.mw-file-element')[0]
# print(soup.select('.mw-file-element')[0])
source=select['src']
print(source)


