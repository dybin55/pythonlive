import count

def create_user(name, age, address):
    print(f"{name}님 환영합니다!")
    dict_1 = {'name' : name,
            'age' : age,
            'address' : address} 
    print(dict_1)
    count_user = count.increase_user()
    print(f"현재 가입된 유저 수: {count_user}")

print(f"현재 가입된 유저 수: {count.increase_user()}")
create_user('홍길동', '30', '서울')
