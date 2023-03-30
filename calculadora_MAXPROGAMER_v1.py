#"\n" serve para pular uma linha e pode ser usado repetidamente.
print("CALCULATOR MAXPROGAMER\n")
print("------- Escolha dois números -------\n")
while True:
    a=float(input("Primeiro número: "))
    print("")
    b=float(input("Segundo número: "))
    print("")
    print("")

    print("Escolha o tipo de conta:\n 1- Divisão\n 2- Multiplicação\n 3- Subtração\n 4- Soma\n\n")
    
    
    TDC = int(input("Você escolheu a operação número: ")) #Tipo de conta
    print("")

    if TDC == 1:
        while b==0:
            print("Escreva um segundo número novamente,\npelas regras matemáticas 0 não pode\nser o denominador de nenhuma conta de\ndivisão.\n")
            b=int(input())
        print(a,"/",b,"=", a/b)     

    elif TDC == 2:
        print(a,"x",b,"=", a*b)

    elif TDC == 3:
        print(a,"-",b,"=", a-b)

    elif TDC == 4:
        print(a,"+",b,"=", a+b)
    else:
        print("\n","------- A operação que foi escolhida é invalida, comece novamente -------","\n")

    parar = input("Se quiser parar a calculadora digite STOP, se não aperte enter.\n")
    if parar == "STOP" or parar == "stop" or parar == "parar" or parar == "Parar":
        print("\n","------- Obrigado por usar a calculadora MAXPROGAMER -------","\n")
        break
    else:
        print ("Escolha novamente dois números:\n")
