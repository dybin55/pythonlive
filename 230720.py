# a = 3

# if a > 4:
#     print('너무 커요')
# else:
#     print('적당해요')


# dust = int(input('미세먼지 수치를 입력하세요 : '))

# if dust > 100:
#     print('밖에 나가지 마세요')
#     if dust > 150:
#         print('이건 좀 심하네;;')
# elif dust > 70:
#     print('마스크 쓰세요')
# else:
#     print('자유롭게 다니세요')


# num = int(input('숫자 : '))

# if num % 2 == 1:
#     print('odd')
# else:
#     print('even')
"""
이거 안되니까 물어보자!
"""


"""for문은 각각의 요소들이 순서대로 변수 인자로 할당되는 구조구나
iterable - dict, set도 순회가능 zip도 사용 가능하겠군"""

# bibles = ['마태', '마가', '누가', '요한']

# for bible in bibles:
#     print(bible)

# for i in range(2):
#     print(i**2)

# numbers = [2, 4, 6, 8, 10]

# for num in range(len(numbers)):
#     numbers[num] = numbers[num] + 1
#     print(numbers)

# a = 1

# while a < 10:
#     print(a)
#     a *= 2

# print('마무리')

# age = int(input('당신의 나이를 입력하세요 : '))

# while age <= 20:
#     if age == 20:
#         print('이제 갓 어른이 되었군요') 
#         break
#     elif age <= 15:
#         print("아직 더 커야겠군요")
#     else:
#         print('좋을 때 입니다')

#     age = int(input('당신의 나이를 입력하세요 : '))

# print("당신의 청소년이 아닙니다")

# for i in range(1,11):
#     if i % 2 == 0:
#        continue
#     print(i)

    

# rgrg = [1,12,3,15,46,48,684,44]

# rgrg_odd = [rg ** 2 for rg in rgrg if rg % 2 == 1]

# print(rgrg_odd)


result = ['하나', '둘', '셋']

print(list(enumerate(result)))

for index, elem in enumerate(result):
    print(index, elem)




