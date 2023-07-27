import create

number_of_people = 0

names = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']


for name in names:
    print(name + '님 환영합니다')


inform = map(create.create_user, names, age, address)


print(list(inform))