def replace_char(string):
    first_char = string[0]
    
    modified_str = first_char + string[1:].replace(first_char, '$')
    return modified_str

str = input("Enter the string:")
result = replace_char(str)
print(result)
