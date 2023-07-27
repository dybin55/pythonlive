def get_value_from_dict(dict_1, key):
    return dict_1.get(key)

my_dict = {'name': 'Alice', 'age': 25}
result = get_value_from_dict(my_dict, 'name')
print(result) # Alice
