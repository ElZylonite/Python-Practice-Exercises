def count_words(text):
    words_count = {}
    for words in text.split():
        words_count[words] = words_count.get(words, 0) + 1
    return words_count

print(count_words("the sun was setting over the quiet town and the birds were singing softly in the trees the wind moved through the leaves and the river flowed calmly past the old bridge the town felt peaceful as the sun continued to set"))