# 1 Faça um programa que vende uma garrafa de água:
    #Se o cliente escolher água mineral natural, será cobrado R$1,50
    #Se o cliente escolher água mineral com gás, será cobrado R$2,50

escolha = int(input("Pressione 1 para água mineral natural ou 2 para água mineral com gás:\n[1/2] "))

if escolha == 1:
    print("Valor a pagar: R$ 1,50")

elif escolha == 2:
    print("Valor a pagar: R$ 2,50")

else:
    print("Faça uma escolha válida.")
