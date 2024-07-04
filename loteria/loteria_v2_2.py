from random import randint

def check_input():
    try:
        return int(input(f"Entre com um número entre 1 e 15 [{3-i} tentativas]: "))

    except ValueError:
        return "Digite um número, animal."


def check_interv(num):
    """Checa se o número está entre o intervalo de 1 e 15. considerando ambos""" # funct's docstring
    return 1 <= num <= 15



def valid_input():
    """Valida a entrada do user para garantir a integridade do código""" # funct's docstring
    while True:

        num = check_input()

        if type(num) != int:
            print(num)
            continue

        if check_interv(num):
            return num


# software's heart
num_sorte = randint(1,15)

for i in range(3):

    num = valid_input()

    if num == num_sorte:
        print("Acertou!")
        break
    elif num > num_sorte:
        print("Errou, tente um número menor")
        continue
    else:
        print("Errou, tente um número maior")
        continue
