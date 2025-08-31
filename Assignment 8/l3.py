mobiles = [
    {'make': 'Nokia', 'model': 216, 'color': 'Black'},
    {'make': 'Mi Max', 'model': '2', 'color': 'Gold'},
    {'make': 'Samsung', 'model': 7, 'color': 'Blue'}
]

sorted_mobiles = sorted(mobiles, key=lambda x: int(x['model']))

print("Original list of dictionaries:", mobiles)
print("Sorted list of dictionaries:", sorted_mobiles)
