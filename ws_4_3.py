import requests
from pprint import pprint as print
import json

# 무작위 유저 정보 요청 경로
API_URL = 'https://jsonplaceholder.typicode.com/users/'
# API 요청
# JSON -> dict 데이터 변환
parsed_data = requests.get(API_URL).json()


# dummy_data_name = []
# dummy_data_company = []
# dummy_data_lat = []
# dummy_data_lng = []

dummy_data = []
for i in range(10):
            # name = parsed_data[i]['name']
            # # dummy_data_name.append(name)
            # company = parsed_data[i]['company']['name']
                # # dummy_data_company.append(company)
            # lat = parsed_data[i]['address']['geo']['lat']
                # # dummy_data_lat.append(lat)
            # lng = parsed_data[i]['address']['geo']['lng']
                # # dummy_data_lng.append(lng)
        # if (-80 < float(parsed_data[i]['address']['geo']['lat']) < 80
        #      and -80 < float(parsed_data[i]['address']['geo']['lng']) < 80):
        
    if (abs(float(parsed_data[i]['address']['geo']['lat'])) < 80
         and abs(float(parsed_data[i]['address']['geo']['lng'])) < 80):
        
        
        user_info = {'company' : parsed_data[i]['company']['name'], 
              'lat' : parsed_data[i]['address']['geo']['lat'], 
              'lng' : parsed_data[i]['address']['geo']['lng'],
              'name' : parsed_data[i]['name']}
        dummy_data.append(user_info)

print(dummy_data)


# def make_dummy_data(i):
#     return {'company' : dummy_data_company[i], 
#               'lat' : dummy_data_lat[i], 
#               'lng' : dummy_data_lng[i],
#               'name' : dummy_data_name[i]}
# dummy_data = []

# for i in range(10):
#     data = make_dummy_data(i)
#     dummy_data.append(data)

