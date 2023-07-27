import requests
from pprint import pprint as print

def request_user(number):
    API_URL = f'https://jsonplaceholder.typicode.com/users/{number}'
    response = requests.get(API_URL)
    parsed_data = response.json()
    data = {
        'name': parsed_data['name'],
        'lat': parsed_data['address']['geo']['lat'],
        'lng': parsed_data['address']['geo']['lng'],
        'company name': parsed_data['company']['name']
    }
    # return parsed_data['name']
    return data

user_list = []
for i in range(1, 11):
    data = request_user(i)
    check_lat = -80 < float(data['lat']) < 80
    check_lng = -80 < float(data['lng']) < 80
    if check_lat and check_lng:
        user_list.append(data)

black_list = ['Hoeger LLC', 'Keebler LLC', 'Yost and Sons', 'Johns Group', 'Romaguera-Crona']

# 수집한 사용자들을 등록하는 함수를 작성하고자 한다.
# 단, 특정 회사에 재직중인 사용자는 제외하고 등록하여야 한다.
# 제시된 black_list에 포함된 company 소속이 아닌 사용자만 등록할 수 있도록 코드를 작성하시오.

'''
- create_user 함수에 사용자 목록을 인자로 넘겨 순회하는 코드를 작성하시오.
- create_user 함수는 넘겨받은 리스트를 순회하여,
  company 이름을 key로, 사용자 이름을 value로 갖는 딕셔너리 censored_user_list를 생성한다.
    - 이 때, value는 리스트로 구성한다.
- create_user 함수를 통해 사용자 목록을 순회하면서, 각 사용자 정보를 censorship 함수에 인자로 넘겨, black_list에 포함 되어 있는지 확인한다.
- censorship 함수는 넘겨받은 회사명이 black_list에 포함되어 있으면 '{회사명} 소속의 {사용자명} 은/는 등록할 수 없습니다.' 문구를 출력하고, False를 반환한다. 포함되어 있지 않다면 '이상 없습니다.' 문구를 출력하고 True를 반환한다.
- censorship 함수의 반환 값을 기준으로 사용자 정보를 딕셔너리 censored_user_list에 담을 것인지 판단한다.
- create_user는 작성 완료된 딕셔너리 censored_user_list를 반환한다.
- 반환 받은 censored_user_list를 출력한다.
'''

def create_user(user_list):
    # print(user_list)
    censored_user_list = {}  # 딕셔너리
    for user in user_list:  # 순서
        # print(user)
        company_name = user['company name']
        name = user['name']
        # key가 딕셔너리에 없으면 => 해당 key를 가지는 데이터를 저장할 list를 내부에 추가
        # if company_name not in censored_user_list: # 딕셔너리 안에 key로 존재하는지 확인
        #     censored_user_list[company_name] = []
        # if censorship(user):
        #     censored_user_list[company_name].append(name)
        if censorship(user):
            if company_name not in censored_user_list: # 딕셔너리 안에 key로 존재하는지 확인
                censored_user_list[company_name] = []
            censored_user_list[company_name].append(name)
    # print(censored_user_list)
    # censored_user_list
    
    # censorship 함수의 반환 값을 기준으로 사용자 정보를 딕셔너리 censored_user_list에 담을 것인지 판단한다.
    # 딕셔너리 censored_user_list를 반환한다.
    return censored_user_list

def censorship(user):
    company_name = user['company name']
    name = user['name']
    # 넘겨받은 회사명이 black_list에 포함되어 있으면
    if company_name in black_list:
        # '{회사명} 소속의 {사용자명} 은/는 등록할 수 없습니다.' 문구를 출력하고, False를 반환한다.
        print(f'{company_name} 소속의 {name} 은/는 등록할 수 없습니다.')
        return False # 이 이후의 작업은 X
    # else:
    # 포함되어 있지 않다면 '이상 없습니다.' 문구를 출력하고 True를 반환한다.
    print('이상 없습니다.')
    return True

# 반환 받은 censored_user_list를 출력한다.

censored_user_list = create_user(user_list) # create_user -> censored_user_list
print(censored_user_list)