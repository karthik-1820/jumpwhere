def remove_char(string, n):
    if n < 0 or n >= len(string):
        return "Invalid index"
    return string[:n] + string[n+1:]

str = input("Enter the String:")
print(remove_char(str, 2))
