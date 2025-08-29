def char_frequency(string):
    freq = {}
    for char in string:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq

str =input("Enter the String:")
result = char_frequency(str)
print(result)
