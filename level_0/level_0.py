#!/usr/bin/python3

# Import HTTP library
import requests

URL = 'http://158.69.76.135/level0.php'
times = 5
votes = 0

# data to send
payload = {
    'id': '1',
    'holdthedoor': 'submit'
}

for i in range(0, times):
    try:
        # start request session
        with requests.Session() as s:

            # send the data
            send = s.post(URL, data=payload)
            print('Post Request made with status: {}'.format(send.status_code))
            # count and print number of votes made
            votes += 1
            if i % 10 == 0:
                print('.')
    except Exception as err:
        print(err)
        i -= 1
print('{} votes have been successful'.format(i + 1))