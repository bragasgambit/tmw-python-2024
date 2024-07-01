# %%
# Lasso de repetição com while
qtd = int(input("Quantos DOOM você quer?\n"))

count = 1
while count <= qtd:
    print("DOOM")
    # vai printar infinitamente, pois nunca chegará a 10
    count += 1          # count = count + 1


# %%
# Lasso eterno While True
while True:
    senha = input("Entre com a senha: ")

    if senha == "senha":
        break # Quebra o lasso e segue com o código

    elif senha == "Yuri":
        print("quase...")
        continue # volta ao início do lasso até sair dela

    else:
        print("foda-se")

print("Saí, finalmente!")

# %%
# Todos os pares entre 1 e 15?

contador = 1
while contador <= 15:
    
    if contador % 2 == 0:
        print(contador)
    
    contador += 1


# %%
