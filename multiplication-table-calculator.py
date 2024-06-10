"""
Variáveis e Funções:
a = tabuada desejada
b = indíce da tabuada (até quando parar a multiplicação)
"""

# Boas-vindas:

print ("\nBem-vindo(a) à Calculadora de tabuada do Raphael\n")
print ("Para iniciar, pressione 'Enter' \nPara sair, digite 's'\n")
a = input ()
while a != "s":

    #Número para tabuada:

    print ("*para sair, entre com 's'* \nInforme-me:\n")
    while True:
        try:
            a = input("Qual será o número para a tabuada: ")
            if a == "s":
                break
            a = float(a)
            break
        except ValueError or TypeError:
            print ("Entre com um número!")
            if a == "s":
                break
    if a == "s":
        break

    # Índice da tabuada:

    b = input ("Qual será o índice da tabuada: ")
    if b == "s":
        break
    while b.isnumeric() == False:
        b = input ("\nEntre com um número inteiro! \nQual será o índice da tabuada: ")
        if b == "s":
            break
    if b == "s":
        break
    b = int(b) + 1

    # Resultado:

    print ("\ntabuada do", a, "de 1 até", b,":\n")
    for b in range (1, b):
        print (a,"*",b,"=", a * b)

    # Sair ou voltar ao Menu Inicial:

    print ("\nPressione 'Enter' para continuar \nPara sair, digite 's'\n")
    a = input ()
    if a == "s":
        break
    print ("")
print ("\nAdeus!")