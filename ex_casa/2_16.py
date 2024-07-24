# Done
# Escreva um programa que solicite ao usuário um número e exiba a tabuada desse número de 1 a 10.

n = int(input("Desired multiplication table of number: "))

for i in range(1,11):
    print(n, "•", i, "=", n * i)
