import requests
import time

# 서버 주소 및 엔드포인트
url_start = 'http://srv1.kitriwhs.kr:15211/api/start'
url_formula_1 = 'http://srv1.kitriwhs.kr:15211/api/formula/'
stage = 1
# 세션 초기화 요청
response_start = requests.get(url_start)
print("API Start Response:")
print(response_start.text)

# 세션 유지하며 첫 번째 스테이지로의 요청
response_formula_1 = requests.get(url_formula_1+str(stage), cookies=response_start.cookies)
print("\nAPI Formula/1 Response:")
print(response_formula_1.text)

