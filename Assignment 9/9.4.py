def shift_to_positive(coords):
    
    min_x = min(x for x, y in coords)
    min_y = min(y for x, y in coords)
    
    shifted = [(x - min_x, y - min_y) for x, y in coords]
    return shifted

coords = [(1, -2), (-2, 4), (-1, -1), (-8, -3), (0, 4), (10, -3)]

result = shift_to_positive(coords)
print(result)
