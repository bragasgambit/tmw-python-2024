# Done
# Faça um programa com uma função que recebe uma frase. Para cada palavra nesta frase, inverta a ordem das letras. Exiba o resultado:
# Esta é a frase original
# atsE é a esarf lanigiro

phrase = input("Type a sentence: ")
# Separate into a list
phrase_list = phrase.split()

# for each word in the list i will invert the order, it will return a list with all words inverted
rev_phrase_list = []
for i in phrase_list:
    rev_phrase_list.append(i[::-1])

# Join the words in the list in a sentence. " " is what I want to glue each word in the list
rev_phrase = " ".join(rev_phrase_list)

print(phrase)
print(rev_phrase)
