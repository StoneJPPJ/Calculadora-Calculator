print("""
    Bem-Vindo!

    Está a calculadora 
    mais potente do mercado.
      
    """)

historico = ""

while True:

    operadores = input("""
    Escolha a operação desejada:

    [+] Soma
    [-] Subtração
    [*] Multiplicação
    [/] Divisão
    [h] Histórico
    [s] Sair
                   
    """)
    
    if operadores == "s":
        break
    
    elif operadores == "+":
        numero1 = float(input("Insira um número: \n"))
        numero2 = float(input("Insira outro número: \n"))
        soma = numero1 + numero2
        historico += f"\nResultado {numero1:.2f} + {numero2:.2f} = {soma:.2f}\n"
        print(f"Seu resultado é: {soma}")

    elif operadores == "-":
        numero1 = float(input("Insira um número: \n"))
        numero2 = float(input("Insira outro número: \n"))
        subtração = numero1 - numero2
        historico += f"\nResultado {numero1:.2f} - {numero2:.2f} = {subtração:.2f}\n"
        print(f"Seu resultado é: {subtração}")

    elif operadores == "*":
        numero1 = float(input("Insira um número: \n"))
        numero2 = float(input("Insira outro número: \n"))
        multiplicação = numero1 * numero2
        historico += f"\nResultado {numero1:.2f} * {numero2:.2f} = {multiplicação:.2f}\n"
        print(f"Seu resultado é: {multiplicação}")

    elif operadores == "/":
        numero1 = float(input("Insira um número: \n"))
        numero2 = float(input("Insira outro número: \n"))
        divisão = numero1 / numero2
        historico += f"\nResultado {numero1:.2f} / {numero2:.2f} = {divisão:.2f}\n"
        print(f"Seu resultado é: {divisão}")

    elif operadores == "h":
        if not historico:
            print ("===============Histórico===============")
            print ("Não foi realizada nenhuma operação." )
            print ("=======================================")
        else:
            print ("===============Histórico===============")
            print (f"{historico}")
            print ("=======================================")

    else:
        print("Operação Inválida.")
