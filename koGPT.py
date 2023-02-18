# coding=utf8
# REST API 호출에 필요한 라이브러리
import requests
import json

# [내 애플리케이션] > [앱 키] 에서 확인한 REST API 키 값 입력
REST_API_KEY = ''

# KoGPT API 호출을 위한 메서드 선언
# 각 파라미터 기본값으로 설정
def kogpt_api(prompt, max_tokens, temperature, top_p, n):
    r = requests.post(
        "https://api.kakaobrain.com/v1/inference/kogpt/generation",
        json = {
            'prompt': prompt,
            'max_tokens': max_tokens,
            'temperature': temperature,
            'top_p': top_p,
            'n': n
        },
        headers = {
            'Authorization': 'KakaoAK ' + REST_API_KEY,
            'Content-Type': 'application/json'
        }
    )
    # 응답 JSON 형식으로 변환
    response = json.loads(r.content)
    return response

# KoGPT에게 전달할 명령어 구성
prompt='''정보:거주지 서울, 나이 30대, 성별 남자, 자녀 두 명, 전공 인공지능, 말투 친절함
정보를 바탕으로 질문에 답하세요.
Q:안녕하세요 반갑습니다. 자기소개 부탁드려도 될까요?
A:안녕하세요. 저는 서울에 거주하고 있는 30대 남성입니다.
Q:오 그렇군요, 결혼은 하셨나요?
A:'''

# 파라미터를 전달해 kogpt_api()메서드 호출


response = kogpt_api(prompt, 20, 1.0, 1.0, 5)
print(response)