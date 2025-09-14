def swap_chars(str1, str2):
    
    if len(str1) < 2 or len(str2) < 2:
        return ("Both strings must have at least 2 characters")
    
    new_str1 = str2[:2] + str1[2:]
    new_str2 = str1[:2] + str2[2:]
    
    return new_str1 + " " + new_str2

str1 = "abc"
str2 = "xyz"
result = swap_chars(str1, str2)
print(result)
