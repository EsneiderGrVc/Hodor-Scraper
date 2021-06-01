# Import HTTP library
import requests

URL = 'http://158.69.76.135/level2.php'
windows_user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'

header = {
    'User-Agent': windows_user_agent,
    'Referer': URL
}

for i in range(5):
    try:
        with requests.Session() as s:
            # get the response object
            r = s.get(URL, headers=header)

            # get key from cookies
            key = s.cookies['HoldTheDoor']

            # compose the data that will send
            payload = {
                'id': '1',
                'key': key,
                'holdthedoor': 'submit'
            }

            # send the data
            r = s.post(URL, data=payload, headers=header)

    except Exception as err:
        print(err)
        i -= 1