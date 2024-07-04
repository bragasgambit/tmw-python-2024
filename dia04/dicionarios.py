# acessar um valor de uma lista é com o índice (apenas número)
# no dicionário o item pode ser acessado com quaisquer caracteres
# lista = []
# dict   = {}
# TUDO no python é objeto

lista = ["Yuri", "Braga", 25]
nome = lista[0]

dados = {"nome":"Yuri",
         "sobrenome":"Braga",
         "idade":25,
         "cores":["azul", "vermelho", "branco"],
         "amigos":[{"nome":"Thales", "idade":"velho"},
                   {"nome":"Paulo", "idade":"mais velho"}]
         #chave:valor
         }

nome = dados["nome"]
print(nome)

print("Idade do Thales é:", dados["amigos"][0]["idade"])

# "dict's" também são conhecidos como "maps" em outras langs

print("Chaves:",dados.keys())     # .keys() retorna as chaves do dict
print("Valores:",list(dados.values()))   # .values() retorna os valores do dict - list() retorna os dados convertidos em uma lista

print("Chave e Valor:",dados.items())

# API é uma interface de comunicação entre sistemas, maps/dicts são muito utilizados para isso
