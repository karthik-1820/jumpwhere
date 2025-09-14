def unique_sorted_words():
    words = input("Enter comma separated words: ")
    word_list = words.split(",")
    unique_words = sorted(set(word.strip() for word in word_list))
    print(",".join(unique_words))
unique_sorted_words()
