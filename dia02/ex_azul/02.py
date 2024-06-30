# 2 Altere o programa anterior para considerar a quantidade de água

escolha = int(input("Pressione 1 para água mineral natural ou 2 para água mineral com gás:\n[1/2] "))
volume = float(input("Indique o volume desejado (em litros):\n "))

if escolha == 1:
    print("O valor a pagar é de R$", 1.5 + round((1 * volume),2))
elif escolha == 2:
    print("O valor a pagar é de R$", round(2.5 + (1.1 * volume),2))

print("Volte sempre!")
