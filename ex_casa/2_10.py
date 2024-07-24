# Done
# Faça um programa que receba um número. Este número corresponde a uma posição na sequência de Fibonacci:
# 0, 1, 1, 2, 3, 5,...
# Exiba o número da sequência cuja posição foi informada:
# A posição x corresponde ao número y

n = 0
number = 0

def fib(n):

    if n in [1]:
        return 0
    elif n in [2]:
        return 1
    return fib(n - 1) + fib(n - 2)

number = int(input("Type a number that correlates to the position in the fibonacci sequence: "))
print(fib(number))

# If I want the hole sequence just uncomment the two lines above:
# for i in range(1, 15 + 1):
    # print(fib(i))
