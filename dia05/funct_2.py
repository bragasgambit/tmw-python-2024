# %%
def soma(a=0, b=0, c=0):
    return a + b + c

print(soma(10, 20, 100))

# inserir uma quantidade indefinida de var
# Resposta: *args = infinitos argumentos em formato de lista

# %%
def soma_n(*args):
    total = 0

    for i in args:
        total += i

    return total

print(soma_n(1,2,3,4,5,6,7,8,9,10))

# %%
def operacao(op, *num):
    total = 0

    if op == "soma":
        for i in num:
            total += i

    elif op == "mult":
        total = 1
        for i in num:
            total *= i

    return total

print(operacao("soma", 1,2,3,4,5,6,7,8,9,10))
print(operacao("mult", 1,2,3,4,5,6,7,8,9,10))

# %%
# Linhas anteriores é o unpack de listas:
dados = ["Yuri", "Braga", 25, 1.70, ["Banana", "Maçã", "Abacate"]]

nome, sobrenome, *_, frutas = dados # primeiro elemento, segundo elemento, o resto é lixo (*_) e o último da lista

print(nome)
print(sobrenome)

# %%
# Em qualquer linguagem de programação inverter a e b se faz assim:
a = 10
b = 20
print(a, b)

c = a
a = b
b = c
print(a, b)

# %%
# No python:
x = 10
y = 20
print(x,y)

x,y = y,x # pois é uma tupla
print(x,y)

# %%
d = 10, 20
type(d)

# %%
