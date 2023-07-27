# ws_5_5.py

# 아래 함수를 수정하시오.

def even_elements(list_1):
    list_2 = []
    while list_1:
        nums = list_1.pop(0)
        print(nums)
    # for nums in list_1:
    #     nums = list_1.pop(0)
        if nums % 2 == 0:
            list_2.extend([nums])
    #     else:
    #         continue
    return list_2
    


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = even_elements(my_list)
print(result)
