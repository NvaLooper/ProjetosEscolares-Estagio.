#Intruções das funções utilizadas:

#while - Como no inglês representa enquanto, serve para criar um loop. Se você quiser parar o loop precisa quebra-lo com a variável Break
#"\n"- Serve para pular uma linha e pode ser usado repetidamente.
#pow - Serve para colocar um número em expoente, o primeiro número é a base e o segundo é o expoente.
#try - Ele tenta fazer o que foi pedido, se não conseguir ele faz volta e tenta novamente. Junto com a função except e finally.
#except - Junto com a função try, ele espera um tipo de erro, se esse erro acontecer ele faz o que você digitar depois dos dois pontos.
#.lower - Serve para deixar todas as palavras que estão na variável ficarem como letra minúscula. (.upper faz o oposto.)

print("CALCULATOR MAXPROGAMER\n")
print("---- Escolha dois números ----\n")
while True:
    try:
        a=float(input("Primeiro número: "))
        print("")
        b=float(input("Segundo número: "))
        print("\n")
    except ValueError:
        print("\n","-------*Você não escolheu números válidos*-------","\n")
    
    else:
        
        print("Escolha o tipo de conta:\n 1- Divisão\n 2- Multiplicação\n 3- Subtração\n 4- Soma\n 5- Potenciação\n 6- Radiciação  \n\n")

        while True:    
            try:
                TDC = float(input("Você escolheu a operação número: ")) #Tipo de conta
                print("")

            except ValueError: 
                print("\n","------- Você não escolheu uma operação válida, tente novamente -------","\n")

            else:
                if TDC == 1:
                    while b==0:
                        print("Escreva um segundo número novamente, pelas regras matemáticas 0\nnão pode ser o denominador de nenhuma conta de divisão.\n")
                        b=int(input())
                    print(a,"/",b,"=", a/b)  
                    break

                elif TDC == 2:
                    print(a,"x",b,"=", a*b)
                    break 

                elif TDC == 3:
                    print(a,"-",b,"=", a-b)
                    break 

                elif TDC == 4:
                    print(a,"+",b,"=", a+b)
                    break

                elif TDC == 5:
                    print(a,"^",b,"=", pow(a,b)) 
                    break

                elif TDC == 6:
                    print("O primeiro número refere ao índice da raiz e o segundo é o valor que será racionalizado")
                    print(b,"√",a,"=", pow(a, 1/b))
                    break

                else:
                    print("\n","------- Você não escolheu uma operação válida, tente novamente -------","\n")
        
        parar = input("Se quiser parar a calculadora digite STOP, se não aperte enter.\n")
        min = parar.lower()
        if min == "stop" or min == "parar":
            print("\n","------- Obrigado por usar a calculadora MAXPROGAMER -------","\n")
            break
        else:
            print ("---- Escolha novamente dois números ----\n")
