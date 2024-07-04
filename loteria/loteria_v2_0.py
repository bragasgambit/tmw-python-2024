def check_input():
    while True:
        try:
            num = int(input(f"Entre com um número entre 1 e 15 [{3-i} tentativas]: "))

        except ValueError:
            print("Digite um número, animal.")
            continue

        if 1 <= num <= 15:
            return num

        else:
            print("Entre com um número válido.")


# Sempre importante definir as funct no início do código para facilitar a manutenção
# Melhorar a função!

num_sorte = 7

for i in range(3):

    num = check_input()

    if num == num_sorte:
        print("Acertou!")
        break
    elif num > num_sorte:
        print("Errou, tente um número menor")
        continue
    else:
        print("Errou, tente um número maior")
        continue

