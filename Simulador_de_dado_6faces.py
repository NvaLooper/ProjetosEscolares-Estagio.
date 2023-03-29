while True:
    Resposta = input("Você gostaria de girar o dado? ")
    if Resposta == "Sim" or Resposta == "sim" or Resposta == "S":
         print("")
         break   
    else:
       print("\n","Ok, quando quiser girar escreva que sim","\n")

while True:
    from random import randint
    print("O número gerado foi:",randint(1,6),"\n")
    GirarNov = input("Você quer gerar um número novamente? ")
    if GirarNov == "Sim" or GirarNov == "sim" or GirarNov == "S":
        print("")
    else:
        break

