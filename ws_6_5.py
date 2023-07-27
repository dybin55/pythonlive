def difference_sets(s_1, s_2):
    # return s_1 - s_2
    return s_1.difference(s_2)

result = difference_sets({1, 2, 3}, {3, 4, 5})
print(result)
