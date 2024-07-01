# Verifica se o item que a pessoa escolheu está na lista:
# laranja, cerveja, miojo, carvão, picanha

lista = "laranja, cerveja, miojo, carvão, picanha"

item = input("O que você quer hoje?\n [laranja, cerveja, miojo, carvão, picanha]\n")

if item in lista:
    print("Dirija-se ao caixa")
else:
    print("Não tem", item)
