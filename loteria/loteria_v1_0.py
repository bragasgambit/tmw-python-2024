# usuário tem que tentar advinhar um número
num = int(input("Entre com um número entre 1 a 15: "))

num_sorte = 7

if num == num_sorte:
    print("Acertou!")

elif num > num_sorte:
    print("Errou, tente um número menor")

else:
    print("Errou, tente um número maior")
