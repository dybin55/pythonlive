def intersection_sets(set_1, set_2):
    # return set_1 & set_2
    return set_1.intersection(set_2)


result = intersection_sets({1, 2, 3}, {3, 4, 5})
print(result) # {3}