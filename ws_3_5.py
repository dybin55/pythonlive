import book
number_of_people = 0

names = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']


def create_user(name, age, address):
    dict_1 = {'name' : name,
            'age' : age,
            'address' : address} 
    # print(f'{name}님 환영합니다!')
    return dict_1

many_user = map(create_user, names, age, address) 
"""
조건에 맞추어 넣어준 dict
"""


# def num_books(age):
#     return age // 10 
"""
lambda함수로 축약함!!1
"""

num_book = list(map(lambda age: age // 10, age))

# print(num_book)

# infos = zip(names, num_book)
# print(list(infos))
# def rental_book(names, num_books):



# info2 = map(rental_book, info)

for name in names:
    print(name + '님 환영합니다!')

# def rental_book(names, num_books):
#     print(f'남은 책의 수 : {book.decrease_book(num_books)}')
#     print(f'{names}님이 {num_book}권의 책을 대여하였습니다')

for name, num in zip(names, num_book):
    print(f'남은 책의 수 : {book.decrease_book(num)}')
    print(f'{name}님이 {num}권의 책을 대여하였습니다')

# for name, num in enumerate(infos):
#     print(f'남은 책의 수 : {book.decrease_book(num)}')
#     print(f'{name}님이 {num}권의 책을 대여하였습니다')