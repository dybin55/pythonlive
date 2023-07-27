# hw_7_2.py

# 아래 클래스를 수정하시오.
class StringRepeater:
   
   
    def repeat_string(self, n, text):
        a = 0
        while a < n:
            print(text)
            a += 1
        '''
        for _ in range(n):
            print(text)
        '''

repeater1 = StringRepeater()
repeater1.repeat_string(3, "Hello")

