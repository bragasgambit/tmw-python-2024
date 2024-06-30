# Números
# 1
# 10.0
# -5
# -7.54

soma = 2 + 2


# Booleans
True
False

condicao = 12 > 18 # True ou False

if condicao:
    print("Isso é verdade")
else:
    print("Isso nunca vai acontecer, pois 12 < 18")


# %%
idade = int(input("Digite sua idade: "))
cnh = input("Você tem CNH? [y/n]")

if idade >= 18 and cnh == "y":
    print("Siga em frente")

else:
    print("Preso em nome da Lei")

condicao = idade >= 18 and cnh == 'sim'
print(condicao) # Só para ver que o output é um boolean


# %%
# True = 1; False = 0
# Em matemática a probalidade de uma coisa E outra acontecer é multiplicação
# Quando for uma coisa OU outra é soma
# and é E (PRODUTO)
# or é OU (SOMA)

print("Esta é a TABELA VERDADE - e/and (produto):")
print("True and True:", bool(1 * 1))
print("False and True:", bool(0 * 1))
print("True and False:", bool(1 * 0))
print("False and False:", bool(0 * 0))

print("E esta é a TABELA VERDADE - ou/or (somatório):")
print("True or True:", bool(1 + 1))
print("True or False:", bool(1 + 0))
print("False or True:", bool(0 + 1))
print("False or False:", bool(0 + 0))

