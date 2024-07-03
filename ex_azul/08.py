# Faça um programa que receba 4 alturas, armazene em uma lista e depois mostre a soma dessas alturas.
altura = []

for i in range(4): # 0, 1, 2, 3 (não toca no 4, para antes)
    a = float(input(f"Entre com a altura em metros {i+1}: ")) # f é formatação de string ie dentro da string add uma var fora do lasso
    altura.append(a)
# a é um valor recebido pelo user

soma = sum(altura)
print(round(soma,2))
