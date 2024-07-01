def bold_txt(txt):
    return "\033[1m" + txt + "\033[0m"

nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")

print("Olá,", bold_txt(nome), 
      "bom saber que você tem", bold_txt(idade), "anos. Seja bem vindo(a)!")

# control characters - in py -> ANSI escape codes
# https://gist.github.com/fnky/458719343aabd01cfb17a3a4f7296797 see comments for a great understand of RGB
