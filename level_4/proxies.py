import requests
from bs4 import BeautifulSoup

s = requests.get('https://www.freeproxylists.net/')
print(s.text, type(s.text))
# soup = BeautifulSoup(s.text, 'html.parser')
# print(soup.xpath('body'))