# após aprender dicionários, o dev vai sair de junior e ser pleno
# problema do sorvetão sem usar if, usando dic

tipo_sorvete = input("Tipo de recipiente:\n"
                       "1 casquinha\n2 cascão\n3 cestinha\n").lower()
sabor = input("Sabor:\n"
              "1 morango\n2 creme\n3 chocolate\n").lower()
cobertura = input("Cobertura?\n"
                  "1 caramelo\n2 morango\n3 chocolate\n4 sem cobertura\n").lower()


sorvetes = {
    "casquinha": 1.00,
    "cascão": 2.50,
    "cestinha":4.00
    #tipo:preço
}


total = 0

if tipo_sorvete in sorvetes:
    total += sorvetes[tipo_sorvete] # acessar a chave do dict sorvetes
else:
    print("Faça uma escolha válida")


coberturas = {"caramelo":1.5,
              "morango":1.5,
              "chocolate":1.5,
              "":0
              #calda:preço
}

if cobertura in coberturas:
    total += coberturas[cobertura]
else:
    print("Faça uma escolha válida")

print("A pagar: R$", total)
