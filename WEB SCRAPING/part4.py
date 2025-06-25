import bs4
import requests
url="https://books.toscrape.com/catalogue/page-{}.html"
page_number=1
while page_number<50:
    request=requests.get(url.format(page_number))
    soup=bs4.BeautifulSoup(request.text,'lxml')
    products=soup.select('.product_pod')
    for product in products:
        rating_tag=product.select_one('.star-rating')
        if 'Two' in rating_tag.get('class',[]):
            title=product.find('h3').find('a')['title']
            print(title)
    page_number+=1