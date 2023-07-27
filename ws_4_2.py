import requests
from pprint import pprint as print

# 무작위 유저 정보 요청 경로
API_URL = 'https://jsonplaceholder.typicode.com/users/'
# API 요청
# JSON -> dict 데이터 변환
parsed_data = requests.get(API_URL).json()

# 응답 데이터 출력
# print(response)
# print(parsed_data[1]['name'])

# def get_name(i):
#     return parsed_data[i]['name']

# name = parsed_data['name']
# print(name)


dummy_data = []
# for i in range(10):
#     name = parsed_data[i]['name']
#     dummy_data.append(name)
"""
내가 푼거
"""

# print(dummy_data)


def request_user(i):
    API_URL = 'https://jsonplaceholder.typicode.com/users/'
    parsed_data = requests.get(API_URL).json()
    dummy_data.append(parsed_data[i]['name'])

for i in range(10):
    request_user(i)

print(dummy_data)

