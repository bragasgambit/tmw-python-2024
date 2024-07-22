from sympy import isprime

n = int(input("Type a number: "))

if isprime(n):
    print(n, "is prime")

else:
    print(n, "is not prime")
