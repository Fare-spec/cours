import requests
from bs4 import BeautifulSoup
def search(url):
    r = requests.get(url)
    return r.text


def search_urls_in_text(content):
    soup = BeautifulSoup(content, 'html5lib')
    hrefs = [a['href'] for a in soup.find_all('a', href=True)]
    return hrefs

print(search_urls_in_text(search("https://google.com")))
