import requests
from bs4 import BeautifulSoup
import queue

atricle_urls = queue.Queue()
pages_urls = []
url = 'http://yuanjian.cnki.net/Search/LiteratureResult?ztcode=J159'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
items = soup.find_all(name='p', attrs={'class': 'tit clearfix'})
for i in items:
    href = i.a['href']
    if "/Article/" in href:
        atricle_urls.put(href)
