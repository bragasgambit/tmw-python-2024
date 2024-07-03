
num_sorte = 7

for i in range(3):

    num = int(input(f"Entre com um número entre 1 a 15 [{3-i} tentativas]: ")) # é importante impedir que o user digite "cinco", por exemplo

    if num == num_sorte:
        print("Acertou!")
        break
    elif num > num_sorte:
        print("Errou, tente um número menor")
        continue
    else:
        print("Errou, tente um número maior")
        continue

# Para evitar que o python quebre:
# try:
    # numero = int(input("Digite um número: "))
# except ValueError as err:
    # print(err) # exibe o erro
    # print("Mano, tu é burro? Pedi um número!")