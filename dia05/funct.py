# y = f(x) = x + 10
# y = f(x) = x * x + 1

# Isso pode ser feito no python com def

def f(x): # definindo a função
    res = x + 10
    return res

y = f(100)
print(y)


def fodase():
    print("foda-se")

fodase() # invocação da função

def soma(a, b=0): # valor obrigatório deve ser definido antes dos opcionais! poderia ser soma(a=0,b=0) - todos os argumentos opcionais
    return a + b

soma(10, 20) # funciona: soma(a=10, b=20), soma(b=20, a=10) e soma(10, b=20) e NÃO funciona: soma(a=10, 20)
soma(10)
