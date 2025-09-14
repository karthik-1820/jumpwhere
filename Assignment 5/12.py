def to_upper(string):
    count = sum(1 for ch in string[:4] if ch.isupper())
    if count >= 2:
        return string.upper()
    return string
print(to_upper("PyThon"))
print(to_upper("PythOn"))
print(to_upper("ABcdxyz"))
