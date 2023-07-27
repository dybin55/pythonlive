# def make_sum(pram1, pram2):
#     """ 이것은 두 수의 
#     합을 반화하는 함수
#     """
#     result = pram1 + pram2 
#     print(f"{result}입니다")

# make_sum(3215, 13210)

# def average(*numb):
#     print(numb)
#     average_total = sum(numb) / len(numb)
#     print(f'평균: {average_total}')


# average(1, 45)


# print(sum(range(100)))


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(12))    

numbers = ['1', '3', '5']
print(list(map(int, numbers)))


print("1" != 1)
print(1.0 == 1)
print(1.0 is 1)
print(31 > 30)


print(5 and 7)
print(7 and 5)

print(3 or 5)

vowel = "aeiou"

print((('b' and 'a')) in vowel)
