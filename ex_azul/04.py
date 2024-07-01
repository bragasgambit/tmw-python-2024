# programa que verifica se a pessoa pertence à familia "Braga"

nome = input("Digite seu nome completo: ")
# tudo no python é objeto, todo objeto tem atributos (características) e métodos (ações)

nome = nome.lower()  # torna todas as letras minúsculas

if "braga" in nome:
    print("Você pertence à família Braga!")

else:
    print("Você não pertence à família Braga.")
