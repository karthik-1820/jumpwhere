def swap_comma_dot(string):
    string = string.replace(',', 'TEMP')
    string = string.replace('.', ',')
    string = string.replace('TEMP', '.')
    return string

str =input("Enter the String")
result = swap_comma_dot(str)
print(result)
