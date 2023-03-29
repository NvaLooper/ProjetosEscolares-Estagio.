#Média dos alunos
Identificação = input("Qual o nome do aluno?\n")
print("")

while True:
        NT1 = float(input("A primeira nota: "))
        print("")
        NT2 = float(input("A segunda nota: "))
        print("")
        NT3 = float(input("A terceira nota: "))
        print("")
        NT4 = float(input("A quarta nota: "))
        print("")
        NT5 = float(input("A quinta nota: "))
        print("")

        if NT1<0 or NT1>20 or NT2<0 or NT2>20 or NT3<0 or NT3>20 or NT4<0 or NT4>20 or NT5<0 or NT5>20:
            print("Notas invalidas, tente novamente:\n")
        else:
            lista = [NT1,NT2,NT3,NT4,NT5]
            media = sum(lista)/5

            print("---------:Informações do aluno:---------\n")
            print("Nome:",Identificação,"\nNotas do aluno:",lista,"\n")
            print("O menor nota é:",min(lista),)

            print("O maior nota é:",max(lista),)

            print("A média do aluno é:",media,"\n")

            if media<10:
                print ("O aluno foi reprovado")
            else:
                print ("O aluno foi aprovado")
            break
        