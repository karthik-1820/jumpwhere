def reverse_multiple(string):
    if len(string) % 4 == 0:
        return string[::-1]   
    else:
        return string

print(reverse_multiple("abcd"))
print(reverse_multiple("python"))
print(reverse_multiple("helloooo"))
