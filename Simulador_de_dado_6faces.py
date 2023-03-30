#Simulação de um dado de 6 faces
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
