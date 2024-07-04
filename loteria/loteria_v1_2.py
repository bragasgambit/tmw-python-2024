num_sorte = 7

for i in range(3):

    try:
        num = int(input(f"Entre com um número entre 1 a 15 [{3-i} tentativas]: ")) # é importante impedir que o user digite "cinco", por exemplo
    except ValueError:
        print("Foi pedido um número, animal.")
        continue # ignora o resto da iteração atual e volta para o início do lasso

    if num == num_sorte:
        print("Acertou!")
        break
    elif num > num_sorte:
        print("Errou, tente um número menor")
        continue
    else:
        print("Errou, tente um número maior")
        continue

# criar um loop para que quando a pessoa digite algo errado, não perca uma tentativa
