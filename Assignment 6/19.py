mixed_list = [10, "apple", 3.14, 25, "banana", 7.5, "orange", 42, 99.9]

int_list = []
str_list = []
float_list = []

for item in mixed_list:
    if isinstance(item, int):
        int_list.append(item)
    elif isinstance(item, str):
        str_list.append(item)
    elif isinstance(item, float):
        float_list.append(item)

print("Original List:", mixed_list)
print("Integers List:", int_list)
print("Strings List:", str_list)
print("Floats List:", float_list)
