# 2 Altere o programa anterior para considerar a quantidade de água

escolha = int(input("Pressione 1 para água mineral natural ou 2 para água mineral com gás: [1/2]\n"))
quantidade = int(input("Quantas garrafas de água você deseja?\n"))
total = 0

if escolha == 1:
    total = 1.5 * quantidade
    
elif escolha == 2:
    total = 2.5 * quantidade

else:
    print("Faça uma escolha valida!")

print("O valor a pagar é de R$", total)
