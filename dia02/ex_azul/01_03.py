# 1 Faça um programa que vende uma garrafa de água:
    #Se o cliente escolher água mineral natural, será cobrado R$1,50
    #Se o cliente escolher água mineral com gás, será cobrado R$2,50
# 2 Altere o programa anterior para considerar a quantidade de água
# 3 Faça o programa de uma sorveteria, onde o usuário pode escolher:
    #Tipo de sorvete: casquinha (R$1,00), cascão (R$2,50), cestinha (R$4,00)
    #Sabor do sorvete: morango, creme, chocolate
    #Cobertura: Caramelo (R$1,50), morango (R$1,50), chocolate (R$1,50), sem cobertura (R$0,00)
#Apresente o valor a ser pago
# %%
escolha = int(input("Pressione 1 para água mineral natural ou 2 para água mineral com gás:\n[1/2] "))

if escolha == 1:
    print("Valor a pagar: R$ 1,50")

elif escolha == 2:
    print("Valor a pagar: R$ 2,50")

else:
    print("Faça uma escolha válida.")



# %%
escolha = int(input("Pressione 1 para água mineral natural ou 2 para água mineral com gás:\n[1/2] "))
volume = float(input("Indique o volume desejado (em litros):\n "))

if escolha == 1:
    print("O valor a pagar é de R$", 1.5 + round((1 * volume),2))
elif escolha == 2:
    print("O valor a pagar é de R$", round(2.5 + (1.1 * volume),2))

print("Volte sempre!")


# %%
recipiente = input("Bem vindo à sorveteria do Braga!\nPor favor, escolha o recipiente:\n"
                       "casquinha\ncascão\ncestinha\n")
sabor = input("Selecione o sabor desejado:\n"
              "morango\ncreme\nchocolate\n")
cobertura = input("Deseja alguma cobertura?\n"
                  "caramelo\nmorango\nchocolate\nsem cobertura")

if recipiente == "casquinha" and cobertura == "caramelo" or "morango" or "chocolate":
    print("R$", float(round(1 + 1.5,2)))
elif recipiente == "casquinha" and cobertura == "sem cobertura":
    print("R$ 1,00")

elif recipiente == "cascao" and cobertura == "caramelo" or "creme" or "chocolate":
    print("R$", 2.5 + 1.5)
elif recipiente == "cascao" and cobertura == 4:
    print("R$ 2,50")

elif recipiente == "cestinha" and cobertura == "caramelo" or "creme" or "chocolate":
    print("R$", float(round(4 + 1.5,2)))
elif recipiente == "cestinha" and cobertura == 4:
    print("R$ 4,00")

else:
    print("Faça uma escolha válida")

# %%
