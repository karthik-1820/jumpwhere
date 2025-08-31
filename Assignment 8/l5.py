is_number = lambda s: s.replace('.', '', 1).isdigit() or (s.startswith('-') and s[1:].replace('.', '', 1).isdigit())
print(is_number("123"))

