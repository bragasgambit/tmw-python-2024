import math

raio = float(input("Digite o raio da circunferência em cm: "))
area = round(math.pi * (raio ** 2),2)
perimetro = round(2 * math.pi * raio,2)

print("A área e o perímetro da circunferência são", area, "cm e", perimetro, "cm respectivamente.")
