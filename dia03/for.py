# %%
# Lasso de repetição com for

for i in "Yuri Braga": # para cada iteração, o i assumirá o valor da coisa que está passando
    if i == "Y":
        continue # pula para a próxima iteração

    elif i == " ":
        continue

    print(i)           # i é uma var

print(i) # mostrará o último valor que foi passado

    
# %%

# Tipo de objeto: str, bool, int, float, range

range(10)  # (start, stop); qtd = stop - start


# Estrutura de dado que pode ser percorrida entre 0 e 10
# começa do zero e vai até o 9
# se eu quiser ir do 1 ao 10: range(1,11)

seq = range(0,10)

for i in seq:
    print(i)

# %%

qtd = int(input("Quantos foda-ses você quer? "))

for i in range(qtd):
    print("foda-se")

# %%
# Resolvendo o problema dos pares (sem while) com for
for i in range(1,16):
    if i % 2 == 0:
        print(i)

# ver ex_azul 08.py para uma excelente utilidade com for