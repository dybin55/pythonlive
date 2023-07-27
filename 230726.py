# class 정의

class Person:
    # 속성(변수)
    blood_color = 'red'

    # 메서드
    def __init__(self, name):
        self.name = name
    # __ 매직 메서드 -> 개발자가 작성하지 않아도 호출이 되는 메서드
    #  생성자 메서드 self는 인스턴스 자기 자신! 


    def singing(self):
        return f'{self.name}이/가 노래합니당.'
    
#  인스턴스 생성

singer_1 = Person('yejin')

print(singer_1.singing())

print(singer_1.blood_color)
print(singer_1.name)


