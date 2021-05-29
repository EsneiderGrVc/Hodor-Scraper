import requests

cheat = {
    'id': 2930,
    'holdthedoor': 'submit'
}

url = 'http://158.69.76.135/level0.php'

for i in range(2):
    hodor = requests.post(url, data=cheat)