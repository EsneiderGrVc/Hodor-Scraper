import requests
from bs4 import BeautifulSoup

get_hodor = requests.get('http://158.69.76.135/level1.php')

soup = BeautifulSoup(get_hodor.text, 'html.parser')
password = (soup.find('input', {'name': 'key'}).get('value'))
print(password)

vote = {'id': '2930', 'key': password, 'holdthedoor': 'submit'}

post_hodor = requests.post("http://158.69.76.135/level1.php", data=vote)