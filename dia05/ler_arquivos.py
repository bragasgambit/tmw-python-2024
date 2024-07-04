# %%
arquivo = open("arquivo.txt", "w+") # w - write line 1, a - add

arquivo.write("\nHello new file")

arquivo.close()


arquivo = open("arquivo.txt", "r")
conteudo = arquivo.read()
linhas = arquivo.readlines()
arquivo.close()

print(linhas)
print(conteudo)

# %%
# sintaxe mais elegante de ler:

with open("arquivo.txt", "r") as file:
    conteudo = file.read()

print(conteudo)

# %%
