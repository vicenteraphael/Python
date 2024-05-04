"""
Variáveis e Funções:
tab = tabuada desejada
index = indíce da tabuada (até quando parar a multiplicação)
msg_adeus()
"""

def msg_adeus():
    print ("\n"); print ("Adeus!")

# Boas-vindas:

print ("\n")
print ("Bem-vindo à Calculadora de Tabuada do Raphael."); print ("\n")
print ("Para iniciar, pressione 'Enter' \nPara sair, digite 's'"); print ("\n")
tab = input (); print ("")
if tab == "s":
    msg_adeus()
while tab != "s":

    #Número para tabuada:

    print ("*para sair, digite 's'* \nInforme-me:"); print ("\n")
    while True:
        try:
            tab = input("Qual será o número para a tabuada: "); print ("\n")
            if tab == "s":
                break
            else:
                tab = float(tab)
                break
        except ValueError or TypeError:
            print ("Entre com um número! \n*para sair, digite 's'*"); print ("\n")
            if tab == "s":
                break
    if tab == "s":
        msg_adeus()
        break

    # Índice da tabuada:

    index = input ("Qual será o índice da tabuada: ")
    if index == "s":
        msg_adeus()
        break
    while index.isnumeric() == False:
        print ("\n")
        index = input ("Entre com um número inteiro! \nQual será o índice da tabuada: ")
        if index == "s":
            break
    if index == "s":
        msg_adeus()
        break
    index = int(index) + 1

    # Resultado:

    print ("\n")
    print ("Tabuada do", tab, "de 1 até", index,":"); print ("\n")
    for index in range (1, index):
        print (tab,"*",index,"=", tab * index)
    print ("\n")

    # Sair ou voltar ao Menu Inicial:

    print ("Pressione 'Enter' para continuar \nPara sair, digite 's'"); print ("\n")
    tab = input ()
    if tab == "s":
        msg_adeus()
        break
    print ("\n")