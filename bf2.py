import requests 
import time

url = 'http://srv1.kitriwhs.kr:13039/call-admin'

int stage = 0
int target_stage = 30

while (stage != 30):
    response = requests.get(url)
    
    a = data.get('a')
    b = data.get('b')
    print(response.text)
    
    result = a+b
    
    data = 


    time.sleep(1)






for i in range(2):
    response = requests.get(url)
    print(response.text)

    nonce_start = response.text.find('nonce=') + len('nonce=')
    nonce_end = response.text.find('"', nonce_start)
    current_nonce = response.text[nonce_start:nonce_end]

    if current_nonce == target_nonce:
        print(f"Find Target")
        break
