import bs4
import requests

num = 1
author_names = []

while True:
    url = f'https://quotes.toscrape.com/page/{num}/'
    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.text, 'lxml')

    if 'No quotes found!' in soup.text:
        break
    
    authors = soup.select('.author')
    for author in authors:
        if author.text not in author_names:
            author_names.append(author.text)
    
    
    num += 1

print(author_names)
