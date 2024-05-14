"""
Variáveis e Funções:
a = tabuada desejada
b = indíce da tabuada (até quando parar a multiplicação)
msg_adeus()
"""

def msg_adeus():
    print ("\n"); print ("Adeus!")

# Boas-vindas:

print ("\n")
print ("Bem-vindo(a) à Calculadora de tabuada do Raphael"); print ("\n")
print ("Para iniciar, pressione 'Enter' \nPara sair, digite 's'"); print ("\n")
a = input (); print ("")
if a == "s":
    msg_adeus()
while a != "s":

    #Número para tabuada:

    print ("*para sair, entre com 's'* \nInforme-me:"); print ("\n")
    while True:
        try:
            a = input("Qual será o número para a tabuada: "); print ("\n")
            if a == "s":
                break
            else:
                a = float(a)
                break
        except ValueError or TypeError:
            print ("Entre com um número! \n*para sair, digite 's'*")
            if a == "s":
                break
    if a == "s":
        msg_adeus()
        break

    # Índice da tabuada:

    b = input ("Qual será o índice da tabuada: ")
    if b == "s":
        msg_adeus()
        break
    while b.isnumeric() == False:
        print ("\n")
        b = input ("Entre com um número inteiro! \nQual será o índice da tabuada: ")
        if b == "s":
            break
    if b == "s":
        msg_adeus()
        break
    b = int(b) + 1

    # Resultado:

    print ("\n")
    print ("tabuada do", a, "de 1 até", b,":"); print ("\n")
    for b in range (1, b):
        print (a,"*",b,"=", a * b)
    print ("\n")

    # Sair ou voltar ao Menu Inicial:

    print ("Pressione 'Enter' para continuar \nPara sair, digite 's'"); print ("\n")
    a = input ()
    if a == "s":
        msg_adeus()
        break
    print ("\n")