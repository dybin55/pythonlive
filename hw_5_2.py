def find_min_max(list_1):
    max_1 = max(list_1)
    min_1 = min(list_1)
    result = (min_1, max_1)
    return result
    

result = find_min_max([3, 1, 7, 2, 5])
print(result) # (1, 7)