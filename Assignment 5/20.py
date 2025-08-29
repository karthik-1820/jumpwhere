def remove_consecutive_duplicates(string):
    result = ""
    for char in string:
        if not result or char != result[-1]:
            result += char
    return result
str =input("Enter the String")
print(remove_consecutive_duplicates(str))
