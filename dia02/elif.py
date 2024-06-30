# %%
idade = int(input("Digite sua idade: "))

if idade < 18:
    print("Você é menor de idade\nVá para casa beber leite!")

elif idade < 35:
    print("Beba com moderação e cuidado para não engravidar!")

elif idade < 70:
    print("Parabéns, você chegou até aqui!\nEspero que não tenha se casado e seja bem sucedido!")

else:
    print("É... Não faça tantos planos para amanhã, que pode nunca chegar; viva o hoje!")

#elif seria um if dentro do else
#if blabla:
    #retorna isso
#else:
    #if blabla:
        #retorna isso
    #else:
        #retorna isso
#Dessa forma a estrutura ficaria muito verborrágica
#Por isso existe o elif

# %%

if 18 <= idade <= 69:
    print("Você é maior de idade.\nBeba à vontade!")

elif idade >= 70:
    print("Se cuida e prepara um plano para a família!")

else:
    print("Você é uma criança. \n Vá para casa!")
