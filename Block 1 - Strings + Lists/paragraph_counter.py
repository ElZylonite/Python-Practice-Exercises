#1er Bloque

paragraph = """
El perro corre veloz por el campo verde mientras el perro busca una pelota 
que el perro quiere morder porque el perro es muy feliz jugando con el 
perro vecino bajo el sol.
"""
word_count = paragraph.split()
longest_word = " "
unique = []
unique_count = 0


for u in word_count:
    if u not in unique:
        unique.append(u)
        unique_count += 1


for i in word_count:
    if len(i) > len(longest_word):
        longest_word = i

print(f"The word count of the paragraph is {len(word_count)} words and the longest word is {longest_word}.")
print(f"The unique count is {unique_count}.")