
# listas continued
# lista vazia -> minha_lista = [] 

minha_lista = ["Yuri", "Braga", 25, 1.70]
print(minha_lista)
# último elemento = lista[-1]
# primeiro lista[0]
# slicing do terceiro elemento ao penúltimo = lista[2:-2]
# step indicando de dois em dois = lista[::2]
# step de trás para frente = lista[::-1]

# Add um item na lista com o método .append():
notas = []
print(notas) # mostrar que é vazio

nota = 7.75

# Add um objeto ao final da lista
notas.append(nota)
# .append() adiciona na lista apenas um único elemento

print(notas) # para ver que a nota entrou na lista

# lista é diferente da função string:
# se usar nome = "Yuri Braga" e quiser usar o método .lower(), eg
# então uma nova var pode ser criada: nome_low = nome.lower() sem alterar a string original

# métodos de lista altera a própria lista
# métodos de string não altera a string mas cria outra string

# adicionar uma lista dentro de uma lista:
# notas.append([2.45, 9.23, 5.00, 1.45])

# .extend()                  - add n elementos
# .append()                  - add um elemento
# concatenação de listas     - notas + [10, 2, 62]     e.g.

notas.extend([2, 7, 31])
print(notas)

notas = notas + [10, 2, 62]
print(notas)

notas.remove(10) # remove a primeira aparição do que se deseja remover
print(notas)

# usar for em listas:
nomes = ["Yuri", "Ester", "Pedro", "Graça", "Tânia"]
for i in nomes:
    print(i.title()) # i é de iteração, mas representa uma var, pode ser qqr coisa

nomes.extend(["Maria Eduarda", "Paulo"])
print(nomes)

dados = [["Yuri", "Renan", "Braga", "Sousa"], 25, 1.70, "Branco", "Brasileiro"]
print("Aqui está seu penúltimo nome:", dados[0][-2])

print("O primeiro caractere do primeiro item da lista dentro da lista é:",dados[0][0][0])
# [Primeiro elemento da lista dados é uma lista][Acessar o primeiro item da lista dentro da lista][O primeiro caractere do item]

