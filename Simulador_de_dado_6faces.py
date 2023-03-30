#Simulação de um dado de 6 faces
while True:
    Resposta = input("Você gostaria de girar o dado? ")
    if Resposta == "Sim" or Resposta == "sim" or Resposta == "S" or Resposta == "s":
         print("")
         break   
    else:
       print("\n","Quando quiser girar o dado escreva que sim(s)","\n")
    
from random import randint
print("O número gerado foi:",randint(1,6),"\n")

while True:
    
    GirarNov = input("Você quer gerar um número novamente? ")
    if GirarNov == "Sim" or GirarNov == "sim" or GirarNov == "S" or GirarNov == "s":
        from random import randint
        print("\n","O número gerado foi:",randint(1,6),"\n")
        
    elif GirarNov == "Não" or GirarNov == "não" or GirarNov == "N" or GirarNov == "n": 
        print("\n","------- Obrigado por jogar :) -------","\n")
        break
    else:
        print("\n","------- Escreva novamente com sim(s) ou não(n) -------","\n")
