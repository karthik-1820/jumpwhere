def longest_word_length(words):
    if not words:
        return 0
    return max(len(word) for word in words)

word_list = ["Python", "Java", "JavaScript", "C"]
result = longest_word_length(word_list)
print("Length of the longest word:", result)
