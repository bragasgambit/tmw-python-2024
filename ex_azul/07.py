# faça um programa que conte quantas vezes a letra “a” aparece em uma palavra
palavra = input("Digite uma palavra: ").lower()

qtd = 0

for i in palavra:
    if i == "a":
        qtd += 1
print("A letra 'a' aparece", qtd, "vez(es) na palavra", palavra)


# Forma utilizando o método .count() da função string
palavra = input("Digite uma palavra: ")
contagem = palavra.count("a")
print("A letra 'a' aparece",contagem,"vez(es) na palavra",palavra)
