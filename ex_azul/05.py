# Saber se a pessoa pertence à família "Braga" ou "Back"

nome = input("Digite seu nome: ")
nome = nome.lower()

if "braga" in nome or "back" in nome:
    print("Você pertence à família Back ou Braga")

else:
    print("Não conheço você")
