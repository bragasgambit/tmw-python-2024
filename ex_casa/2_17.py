# Done
# Escreva um programa que solicite ao usuário uma palavra e verifique se a palavra é um palíndromo (ou seja, é a mesma palavra quando lida de trás para frente).
# This function returns the reverse of a string:
def palindrome(word):
    return word == word[::-1]

word = input("Type a word: ").lower()

drow = palindrome(word)

if drow:
    print(f"The word {word} is a palindrome")
else:
    print(f"{word} is not a palindrome")
