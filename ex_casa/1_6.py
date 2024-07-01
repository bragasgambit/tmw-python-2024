selecione = int(input("Conversor de minutos e segundos no formato [hr:min:seg]\n"
                     "Você quer colocar em minutos (1) ou segundos (2)?\n"))

if selecione == 1:
    minutos = int(input("Digite um número em minutos: "))

    
    horas = minutos // 60 # horas inteiras
    
    minutos = minutos % 60 # resto da divisão de horas
    
    
    print(horas, ":", minutos, ":00",sep="") # sep é o espaçamento entre argumentos da função print


elif selecione == 2:
    segundos = int(input("Digite um número em segundos: "))
    

    horas = segundos // (60*60) # pega a inteira parte da divisão com //

    segundos = segundos % (60*60) # resto da divisão

    minutos = segundos // 60 # minutos inteiros

    segundos = segundos % 60 # resto de segundos da divisão por min


    print(horas,minutos,segundos, sep=":")

else:
    print("Faça uma escolha válida")