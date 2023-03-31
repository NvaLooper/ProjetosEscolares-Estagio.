#Intruções das funções utilizadas:

#while - Como no inglês representa enquanto, serve para criar um loop. Se você quiser parar o loop precisa quebra-lo com a variável Break.
#try - Ele tenta fazer o que foi pedido, se não conseguir ele faz volta e tenta novamente. Junto com a função except e finally.
#except - Junto com a função try, ele espera um tipo de erro, se esse erro acontecer ele faz o que você digitar depois dos dois pontos.
#.lower - Serve para deixar todas as palavras que estão na variável ficarem como letra minúscula. (.upper faz o oposto.)
#"\n"- Serve para pular uma linha e pode ser usado repetidamente.
#sum - Soma os números dentro de uma lista.
#min/max - Pega o menor ou o maior número da lista.

Identificação = input("Qual o nome do aluno? ")
print("")

while True:
    try:
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
        
    except ValueError:
        print("\n","A nota deve ser escrita em números, tente novamente.","\n")

    else:
    
        if NT1<0 or NT2<0 or NT3<0 or NT4<0 or NT5<0:
            print("Nota(s) invalida(s), o aluno não pode ter tirado menos que 0, tente novamente:\n")

        elif NT1>20 or NT2>20 or NT3>20 or NT4>20 or NT5>20:
            print("Nota(s) invalida(s), o aluno não pode ter tirado mais que 20, tente novamente:\n")

        else:
            lista = [NT1,NT2,NT3,NT4,NT5]
            media = sum(lista)/5 #"Sum" soma todos os números da lista

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
