

def check_number():
    while True:
        try:
            num = int(input('숫자를 입력하시오 : '))
            if num >= 0:
                print('양수입니다.')
            elif num == 0:
                print('0입니다.')
            else:
                print('음수입니다.')
        
        except ValueError:
            print('잘못된 입력입니다.') 
            break
 
check_number()
