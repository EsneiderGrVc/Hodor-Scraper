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
api_key = '174faff8fbc769e94a5862391ecfd010'

for i in range(5):
# start request session
    with requests.Session() as s:
        # get the response object
        response = s.get(URL, headers=header)

        # get image response object
        image = s.get(captcha_url, headers=header)

        # write captcha file
        image_file = open('captcha.png', 'wb')
        image_file.write(image.content)
        image_file.close()

        # Resolve captcha with pytesseract
        captcha = pytesseract.image_to_string(Image.open('captcha.png'))
        captcha = captcha.replace(" ", "").strip()

        # get key from cookies
        site_key = response.cookies['HoldTheDoor']

        # compose the data that will send
        payload = {
            'id': '1',
            'key': site_key,
            'captcha': captcha,
            'holdthedoor': 'submit'
        }
        #
        send = s.post(URL, headers=header, data=payload)
