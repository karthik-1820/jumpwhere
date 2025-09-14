def check_start(string, prefix):
    return string.startswith(prefix)

print(check_start("Hello World", "Hello"))
print(check_start("Hello World", "Hi"))
print(check_start("python programming", "py"))
