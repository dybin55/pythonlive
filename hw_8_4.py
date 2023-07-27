class UserInfo:
    def __init__(self):
        self.user_data = {}
    
    def get_user_info(self):
        
        try:
            self.name = input("이름를 입력하세요 : ")
            self.age = int(input("나이를 입력하세요 : "))
            # print(f'사용자 정보: \n이름 : {self.name} \n나이 : {self.age}세')
        except ValueError:
            print("나이는 숫자로 입력해야 합니다.")

    def display_user_info(self):
        try:
            self.user_data.update({self.name : self.age}) 
            print(f'사용자 정보: \n이름 : {self.name} \n나이 : {self.age}세')
        except:
            print('사용자 정보가 입력되지 않았습니다.')

user = UserInfo()
user.get_user_info()
user.display_user_info()