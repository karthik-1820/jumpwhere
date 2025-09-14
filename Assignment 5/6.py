def add_ing(string):
    if len(string) < 3:
        return string
    elif string.endswith("ing"):
        return string + "ly"
    else:
        return string + "ing"

print(add_ing("play"))
print(add_ing("playing"))
