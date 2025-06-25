import bs4
import requests
request=requests.get('https://example.com')
soup=bs4.BeautifulSoup(request.text,'lxml')
print(soup)
print(soup.select('h1'))
print(soup.select('h1')[0].getText())