def smallest_largest_word(string):
    words = string.split()
    smallest = min(words, key=len)
    largest = max(words, key=len)
    return smallest, largest

str =input("Enter the String")
smallest, largest = smallest_largest_word(str)
print("Smallest word:", smallest)
print("Largest word:", largest)
