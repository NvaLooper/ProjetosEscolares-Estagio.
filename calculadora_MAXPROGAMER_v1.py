#"\n" serve para pular uma linha e pode ser usado repetidamente.
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
        
        print("Escolha o tipo de conta:\n 1- Divisão\n 2- Multiplicação\n 3- Subtração\n 4- Soma\n\n")
        TDC = int(input("Você escolheu a operação número: ")) #Tipo de conta
        print("")

        print("\n","Você não escolheu uma operação válida, tente novamente.","\n")

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
        
    parar = input("Se quiser parar a calculadora digite STOP, se não aperte enter.\n")
    min = parar.lower()
    if min == "stop" or min == "parar":
        print("\n","------- Obrigado por usar a calculadora MAXPROGAMER -------","\n")
        break
    else:
        print ("---- Escolha novamente dois números ----\n")
