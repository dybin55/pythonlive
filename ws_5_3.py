# ws_5_3.py

# 아래 함수를 수정하시오.
def sort_tuple(arg):
  
#   new_list = list(arg)
#   new_list.sort()
#   new_tuple = tuple(new_list)
    new_tuple = tuple(sorted(arg))

  
    return new_tuple

result = sort_tuple((5, 2, 8, 1, 3))
print(result)
