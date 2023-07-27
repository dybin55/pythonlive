# ws_5_2.py

# 아래 함수를 수정하시오.
def remove_duplicates(list_1):
    new_lst = list(set(list_1))
    return new_lst

result = remove_duplicates([1, 2, 2, 3, 4, 4, 5])
print(result)
