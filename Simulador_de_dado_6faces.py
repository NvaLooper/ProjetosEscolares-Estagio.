#Introdução das funções utilizadas:

#while - Como no inglês representa enquanto, serve para criar um loop. Se você quiser parar o loop precisa quebra-lo com a variável Break
#.lower - Serve para deixar todas as palavras que estão na variável ficarem como letra minúscula. (.upper faz o oposto.)
#from random import randint - Da biblioteca random importa a função randint
#randint - Gera números aleatórios, dentro dos números que você colocar como limite. 

while True:
    Resposta = input("Você gostaria de girar o dado? ")
    minR = Resposta.lower()
    if minR == "sim" or minR == "s":
         print("")
         break   
    else:
       print("\n","Quando quiser girar o dado escreva que sim(s)","\n")
    
from random import randint
print("O número gerado foi:",randint(1,6),"\n")

while True:
    
    GirarNov = input("Você quer gerar um número novamente? ")
    minG = GirarNov.lower()
    if minG == "sim" or minG == "s":
        from random import randint
        print("\n","O número gerado foi:",randint(1,6),"\n")
        
    elif minG == "não" or minG == "n": 
        print("\n","------- Obrigado por jogar :) -------","\n")
        break
    else:
        print("\n","------- Escreva novamente com sim(s) ou não(n) -------","\n")
