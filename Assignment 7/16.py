my_dict = {'a': 50, 'b': 20, 'c': 90, 'd': 70, 'e': 40}

print("Original Dictionary:", my_dict)

highest_values = sorted(my_dict.values(), reverse=True)[:3]

print("Top 3 highest values:", highest_values)
