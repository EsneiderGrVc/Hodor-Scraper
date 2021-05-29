import requests

URL = 'http://158.69.76.135/level1.php'

for i in range(10):
    with requests.Session() as s:
        # get the response object
        s.get('http://158.69.76.135/level1.php')

        #get key from cookies
        password = s.cookies['HoldTheDoor']

        #compose the data that will send
        payload = {
            'id': 1,
            'key': password,
            'holdthedoor': 'submit'
        }

        #send the data
        s.post(URL, data=payload)