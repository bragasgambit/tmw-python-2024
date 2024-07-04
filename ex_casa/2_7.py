frutas = {"Maçã":1.50,
          "Banana":2.75,
          "Uva":1.90,
          "Pera":1.25,
          "Laranja":0.65,
          "Limão":1.25,
          "Goiaba":2.15,
          "Abacaxi":3.20,
          "Jaca":5.80
}

while True:
    fruta_user = input("Escolha uma fruta:\n[Maçã, Banana, Uva, Pera, Laranja, Limão, Goiaba, Abacaxi, Jaca]\n").title()

    if fruta_user in frutas:
        print("R$",frutas[fruta_user]) # chamar um dict é com: dict["chave"]
        continue

    elif fruta_user == "":
        break

    else:
        print("Faça uma escolha válida!")
        continue

print("Volte sempre")
