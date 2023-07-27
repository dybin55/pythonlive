def get_keys_from_dict(dict_1):
    return list(dict_1.keys())
    
my_dict = {'name': 'Alice', 'age': 25}
result = get_keys_from_dict(my_dict)
# for key in result:
#     print(key)
print(result)