num_sorte = 7

for i in range(3):

    while True:
        try:
            num = int(input(f"Entre com um número entre 1 a 15 [{3-i} tentativas]: ")) # é importante impedir que o user digite "cinco", por exemplo
            break
        except ValueError:
            print("Digita um número, animal.")

    if num == num_sorte:
        print("Acertou!")
        break
    elif num > num_sorte:
        print("Errou, tente um número menor")
        continue
    else:
        print("Errou, tente um número maior")
        continue

# 03.07.2024