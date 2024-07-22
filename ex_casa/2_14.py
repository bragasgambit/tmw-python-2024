# Done
# Considere a seguinte lista:
# [123, 435, 987, 1984, 2, 19, 423, -178, 320]
# Faça um programa que retorne a posição do menor e do maior valor encontrado:
# O maior valor está na posição x
# O menor valor está na posição y

list = [123, 435, 987, 1984, 2, 19, 423, -178, 320]

print(f"O maior valor está na posição {list.index(max(list))}, número {list[list.index(max(list))]}, inicinado a contagem do 0")

print(f"O menor valor está na posição {list.index(min(list))}, número {list[list.index(min(list))]}")
