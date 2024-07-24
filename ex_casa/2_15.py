# Done
# Escreva um programa que receba uma lista de números do usuário e conte quantas vezes um número específico aparece na lista. Solicite ao usuário um número e exiba a contagem.

# Actually I am counting strings. That are string number inputed by the user
list = []
list.extend(input("Type some numbers without spaces: "))

n = input("Select a number from 0 to 9: ")
count = 0
count = list.count(n)

print(f"The selected number, {n}, appears {count} times in your list.")
