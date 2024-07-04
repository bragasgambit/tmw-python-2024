# in bash: $ pip install requests
# %%
import requests
import pandas as pd

url = "https://api.opendota.com/api/heroes"
resposta = requests.get(url)

resposta.status_code
# %%

dados = resposta.json() # JavaScript Object Notation

# %%

dados # lista de dicts, portanto pode ser acessado como uma lista

# %%
dados[0]['localized_name']
# %%
for i in dados:
    print(i["localized_name"]) # exibe todos os nomes dos personagens da lista
# %%

df = pd.DataFrame(dados)
# %%
df.to_csv("heroes_dota.csv",sep=";")
# %%
# Obter uma .csv a partir de uma API
url = "https://api.opendota.com/api/proMatches"
data = requests.get(url).json()
df_partida = pd.DataFrame(data)
df_partida.to_csv("partidas_dota_proplayers.csv", sep=";")

# %%
