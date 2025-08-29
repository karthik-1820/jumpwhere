def first_last_chars(string):
    if len(string) < 2:
        return ""
    return string[:2] + string[-2:]

str = input("Enter the String:")
result = first_last_chars(str)
print(result)
