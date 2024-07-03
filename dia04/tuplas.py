# lista - índice            - list  = [a,b,c,...,n]
# dict  - chave             - dict  = {a:b,...,m:n}
# tupla - índice (imutável) - tuple = (a,b,c,...,n)
#def tupla == listas imutáveis
# utilizado quando um dado está sendo manipulado e quero garantir que o mesmo não será alterado

nomes = ("Yuri", "Ester", "Paulo") # isso é uma tupla, imutável
print(nomes)

nomes[:] # tuplas podem ser navegadas
nomes[::-1] # se alterar, cria uma tupla nova