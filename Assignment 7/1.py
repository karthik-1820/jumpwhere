my_dict = {'apple': 10, 'banana': 5, 'orange': 7, 'mango': 20, 'grapes': 15}

asc_sorted = dict(sorted(my_dict.items(), key=lambda item: item[1]))

desc_sorted = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))

print("Original Dictionary:", my_dict)
print("Ascending Order:", asc_sorted)
print("Descending Order:", desc_sorted)
