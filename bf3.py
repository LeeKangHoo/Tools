#!/usr/bin/python3
import requests
import time

# 서버 주소 및 엔드포인트
url_start = 'http://srv1.kitriwhs.kr:15211/api/start'
url_formula = 'http://srv1.kitriwhs.kr:15211/api/formula/'

# 세션 초기화 요청
response_start = requests.get(url_start)
print("API Start Response:")
print(response_start.text)

# 세션 유지하며 스테이지 진행
for stage in range(1, 31):
    time.sleep(1)
    print("Stage:", stage)

    # 세션 쿠키 정보 출력
    print("Session cookies:", response_start.cookies)

    # 스테이지마다 숫자를 받아옴
    response_formula_get = requests.get(url_formula + str(stage), cookies=response_start.cookies)
    data = response_formula_get.json()

    # Formula GET 응답과 세션 쿠키 출력
    print("Formula GET Response Text:", response_formula_get.text)
    print("Formula GET Session cookies:", response_formula_get.cookies)

    # 'a'와 'b'가 None이 아닌지 확인
    if 'a' in data and 'b' in data:
        a = data['a']
        b = data['b']

        # 계산된 answer 값을 서버로 전송
        answer = a + b
        response_formula_post = requests.post(url_formula + str(stage), data={'answer': answer}, cookies=response_start.cookies)

        # 서버 응답 확인
        print("Formula POST Response:", response_formula_post.text)

        # 다음 스테이지로 진행
        print(f"Moving to next stage: {stage + 1}")
    else:
        print("Invalid response format")

