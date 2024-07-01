# Operador lógico - if/else

idade = int(input("Digite sua idade: "))

if idade >= 18:     # condição lógica (True/False - boolean)
    print("Você é maior de idade") # 4 espaços para identação (identation)
    print("Beba à vontade!")
    # Só executa se a condição lógica for True
# Não pode ter nada entre o if e o else

else:
    print("Você é menor de idade\nBeba leite!")
    print("Volte em", 18 - idade, "ano(s)!")
    # Só pode existir um else se estiver conectado a um if
