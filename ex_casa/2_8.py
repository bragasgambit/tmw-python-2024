import math
notas = []

for i in range(4):
    nota = float(input(f"Digite a nota {i+1}: "))
    notas.append(nota)

average = round(math.fsum(notas)/len(notas),2)
menor = min(notas)
maior = max(notas)
print("Média:", average)
print("Menor:", menor)
print("Maior:", maior)
