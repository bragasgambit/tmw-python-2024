nome = input("Nome: ").title()
idade = int(input("Idade: "))

if idade < 18:
    print(nome,", você não pode dirigir nem beber!",sep="")

elif idade < 65:
    print(nome, ", bebida liberada! Só não vale dirigir!",sep="")

else:
    print(nome, ", beba com muita moderação!",sep="")
