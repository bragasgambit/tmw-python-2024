negrito_init = "\033[1m"
negrito_end = "\033[0;0m"

nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")

print("Olá,", negrito_init + nome + negrito_end, "bom saber que você tem", negrito_init + idade + negrito_end, "anos. Seja bem vindo(a)!")