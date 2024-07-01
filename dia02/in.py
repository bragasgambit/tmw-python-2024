# Operador lógico - in

nome = "Yuri Braga"

print("Yuri" in nome)
print("Ester" in nome)


# Do exercício_azul 03:

recipiente = int(input("Tipo de recipiente:\n"
                       "1 casquinha\n2 cascão\n3 cestinha\n"))
sabor = int(input("Sabor:\n"
              "1 morango\n2 creme\n3 chocolate\n"))
cobertura = int(input("Cobertura?\n"
                  "1 caramelo\n2 morango\n3 chocolate\n4 sem cobertura\n"))
total = 0 # valor começa em 0 e conforme os ingredientes são escolhidos, o valor aumenta


# Parte do recipiente
if recipiente == 1:
    total = total + 1

elif recipiente == 2:
    total += 2.5 # var += 1 significa que a variável atribuída antes da condição lógica é resgatada e atribuída a soma de 1

elif recipiente == 3:
    total += 4

else:
    print("Faça uma escolha válida")

# Parte da cobertura original do exercício
    #if cobertura == 1:
        #total += 1.5 # a partir da condição lógica anterior, o total será resgatado dela e acrescido o valor de 1.5
#
    #elif cobertura == 2:
        #total += 1.5
#
    #elif cobertura == 3:
        #total += 1.5
#        
    #elif cobertura == 4:
        #pass # só passa/não faz nada
#
    #else:
        #print("Faça uma escolha válida")

coberturas = 1,2,3

if cobertura in coberturas:
    total += 1.5

elif cobertura == 4:
    pass

else:
    print("Faça uma escolha válida")

print("A pagar: R$", total)