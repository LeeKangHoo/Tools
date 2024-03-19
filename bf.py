import requests 
import time

url = 'http://srv1.kitriwhs.kr:13039/call-admin'
target_nonce='4c'


for i in range(2):
    response = requests.get(url)
    print(response.text)

    nonce_start = response.text.find('nonce=') + len('nonce=')
    nonce_end = response.text.find('"', nonce_start)
    current_nonce = response.text[nonce_start:nonce_end]

    if current_nonce == target_nonce:
        print(f"Find Target")
        break
