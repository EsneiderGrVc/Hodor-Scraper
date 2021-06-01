import requests

URL = 'http://158.69.76.135/level4.php'
WINDOWS_USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'

header = {
    'User-Agent': WINDOWS_USER_AGENT,
    'Referer': URL
}
proxy_list = []

# set proxy_list
with open('./proxy_list.txt', 'r') as proxies:
    i = 0
    for line in proxies:
        proxy_list.append({'http': line[:-1]})
        # proxy_list['{}'.format(i)] = line[:-1]
        i += 1

for proxy in range(60, 70):
    try:
        # start requests session
        with requests.Session() as s:
            # get the response object
            print('Getting a Response Object: ...')
            response = s.get(URL, headers=header, proxies=proxy_list[proxy])
            print(' - Object Obtained with status: {}'.format(response.status_code))

            # get key from cookies
            key = response.cookies['HoldTheDoor']

            # compose data that will send
            payload = {
                'id': '1',
                'key': key,
                'holdthedoor': 'submit'
            }

            # send data
            send = s.post(URL, headers=header, proxies=proxy_list[proxy], data=payload)
            print('Post Request made with status: {}'.format(send.status_code))
            print('--------------------------------------')
    except Exception as err:
        print('Something went wrong =(')
