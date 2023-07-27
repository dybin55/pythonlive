# set_1 = {2, 4, 8}

# a = set_1.pop()
# print(set_1)
# print(a)

# set_1.update([10])

# set_1.add(6)

# set_1.pop()
# print(set_1)


# # set_1 = {'a', 'b', 'c', 'd', 'e'}
# # set_2 = {'l', 'o', 'v', 'e'}

# # print(set_1.issuperset(set_2))
# # print(set_1.issubset(set_2))
# # print(set_1.union(set_2))
# # print(set_1 - set_2)
# # print(set_1 | set_2)




blood_type = ['A', 'B', 'A', 'AB', 'A', 'A','B','O','B' ]

# new_dict = {}
# for types in blood_type:
#     if types in new_dict:
#         new_dict[types] += 1
    
#     else:
#         new_dict[types] = 1

# print(new_dict)

# new_dict = {}
# for types in blood_type:
#     new_dict[blood_type] = new_dict.get(blood_type, 0) + 1

# print(new_dict)

new_dict = {}
for types in blood_type:
    new_dict.setdefault(blood_type, 0)
    new_dict[blood_type] += 1
    
print(new_dict)
