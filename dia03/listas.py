# Forma de armazenar vários valores diferentes em uma var?
# com listas - Lista é um conjunto de valores

# %%
minha_lista_vazia = []

# lista != array -> na mesma lista pode conter mais de um tipo de objeto, mas só pode conter um tipo no mesmo array
minha_lista = ['Yuri', 'Braga', 25, 1.70] # lista com 4 elementos e 3 objetos diferentes
print(minha_lista)


# %%
# Acessar valores no py

minha_lista[0] # índice 0 da lista (SEMPRE o 1o indice é o 0)
# só funciona com números inteiros
# %%
minha_lista[1]
# %%
indice = len(minha_lista)-1
minha_lista[indice] # último elemento da lista
# %%

minha_lista[-1] # pega o tamanho da lista e coloca -1

# %%
minha_lista[-2] # penúltimo elemento
# %%

# Slicing lista

minha_lista[0:2] # fatiamento de lista pegando dois elementos
# começa de onde quer e para um antes
# segundo elemento e o terceiro: minha_lista[1:3]
# todos os elementos menos o último: minha_lista[0:-1]

# %%
# fatiar do início à metade da lista:
minha_lista[0:int(len(minha_lista)/2)]
# %%

# Se quer começar do 0 não precisa exibir o primeiro valor:
minha_lista[:] # do início ao fim

# %%

minha_lista[::2] # start:stop:step
# começa do 0, vai até o -1 (último da lista), mas imprime pulando um, portanto, só os ímpares
# caso quisesse imprimir apenas os pares: minha_lista[1::2]


# %%
# exibe ao contrário:
minha_lista[::-1]
# exibir ao contrário pulando um: minha_lista[::-2]
