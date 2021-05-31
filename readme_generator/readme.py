import requests
from bs4 import BeautifulSoup

SIGN_IN_URL = input(str('Here goes the url project: '))

with requests.Session() as s:
    response = s.get(SIGN_IN_URL)
    soup = BeautifulSoup(response.text, 'html.parser')
    form = soup.find_all('input')
    key = soup.find('input', {'name': 'authenticity_token'}).get('value')
    payload = {
        'user[login]': '2930@holbertonschool.com',
        'user[password]': 'Ag10624943',
        'authenticity_token': key,
        'user[remember_me]': '1',
        'commit': 'submit'
    }
    send = s.post(SIGN_IN_URL, data=payload)

    project = s.get('https://intranet.hbtn.io/projects/246')

    with open('./README.md', 'w') as f:
        f.write(project.text)
    print('----------------------------------------------------------------')
    print('\nYour README file has been generated succesfully, so please...')
    print('BUY ME A COFFEEEEEEEEEEEEEEEE! -______-\n')
    print('----------------------------------------------------------------')