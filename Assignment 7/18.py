def check_all_empty(dict_list):
    return all(len(d) == 0 for d in dict_list)

list1 = [{}, {}, {}]
list2 = [{1: 2}, {}, {}]

print("List1:", list1, "->", check_all_empty(list1))
print("List2:", list2, "->", check_all_empty(list2))
