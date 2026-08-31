text = """
the sun was setting over the quiet town and the birds were singing softly
in the trees the wind moved through the leaves and the river flowed calmly
past the old bridge the town felt peaceful as the sun continued to set
"""

words_count = {}

for words in text.split():
    words_count[words] = words_count.get(words, 0) + 1

most_repeated_words = sorted(words_count.items(), key=lambda x: x[1], reverse=True)
top_three = most_repeated_words[:3]

print(words_count)
print(most_repeated_words)
print(top_three)