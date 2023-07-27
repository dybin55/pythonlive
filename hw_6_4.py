def add_item_to_dict(dict_1, k, v):
    dict_1.setdefault(k, v)
    return dict_1
my_dict = {'name': 'Alice', 'age': 25}
result = add_item_to_dict(my_dict, 'country', 'USA')
print(result)
