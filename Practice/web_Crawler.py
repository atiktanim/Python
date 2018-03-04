'''
import requests
from bs4 import BeautifulSoup

def trade_spider(max_pages):
    page = 1
    while page <= max_pages:
        url = ''+str(page)
        source_code=requests.get(url)
        plain_text=source_code.text
        soup = BeautifulSoup(plain_text)
        for link in soup.finalAll('a',{'class':'product-item'}):
            href=link.get('href')
            print(href)
        page=+1

trade_spider(1)

'''



from bs4 import BeautifulSoup
