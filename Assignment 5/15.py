from collections import Counter
def count_repeated_chars(string):
    
    freq = Counter(string)
    repeated = {char: count for char, count in freq.items() if count > 1}
    return repeated

sample_str = "thequickbrownfoxjumpsoverthelazydog"
result = count_repeated_chars(sample_str)
print(result)
