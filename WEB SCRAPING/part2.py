import bs4
import requests
request=requests.get('https://en.wikipedia.org/wiki/Grace_Hopper')
soup=bs4.BeautifulSoup(request.text,'lxml')
# print(soup)
for tag in soup.select('div.mw-heading.mw-heading3'):
    print(tag.get_text())

# class="mw-heading mw-heading4">…</div>
