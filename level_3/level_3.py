"""
    Imports:
        requests:
            HTTP library
        pytesseract:
            Optical Character Recognition (OCR) library
        PIL:
            Image processing library
"""


import requests
import pytesseract
try:
        from PIL import Image
except ImportError:
        import Image

URL = 'http://158.69.76.135/level3.php'
captcha_url = 'http://158.69.76.135/captcha.php'
windows_user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
header = {
    'User-Agent': windows_user_agent,
    'Referer': URL
}
times = 5
api_key = '174faff8fbc769e94a5862391ecfd010'

for i in range(times):
    try:
        # start request session
        with requests.Session() as s:
            # get the response object
            print('Getting a Response Object: ...')
            response = s.get(URL, headers=header)
            print(' - Object Obtained with status: {}'.format(response.status_code))
            # get image response object
            image = s.get(captcha_url, headers=header)

            # write captcha file
            image_file = open('captcha.png', 'wb')
            image_file.write(image.content)
            image_file.close()

            # Solve captcha with pytesseract
            captcha = pytesseract.image_to_string(Image.open('captcha.png'))
            captcha = captcha.replace(" ", "").strip()
            print(' - Captcha solved!')

            # get key from cookies
            key = response.cookies['HoldTheDoor']

            # compose the data that will send
            payload = {
                'id': '1',
                'key': key,
                'captcha': captcha,
                'holdthedoor': 'submit'
            }

            # send data
            send = s.post(URL, headers=header, data=payload)
            print('Post Request made with status: {}'.format(send.status_code))
            print('--------------------------------------')
    except Exception as err:
        print('Something went wrong =(')
        i -= 1