def not_poor(string):
    not_pos = string.find('not')
    poor_pos = string.find('poor')

    if not_pos != -1 and poor_pos != -1 and not_pos < poor_pos:
        return string[:not_pos] + 'good' + string[poor_pos + 4:]
    else:
        return string

print(not_poor("The movie is not that poor!"))
print(not_poor("This dinner is poor but tasty"))
