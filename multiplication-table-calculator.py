def msg_adeus():
    print ("\n"); print ("Adeus!")
print ("\n")
print ("Bem-vindo à Calculadora de Tabuada do Raphael."); print ("\n")
print ("Para iniciar, pressione 'Enter' \nPara sair, digite 's'"); print ("\n")
tab = input (); print ("")
if tab == "s":
    msg_adeus()
while tab != "s":
    #Número para tabuada:

    print ("Qual será o número para a tabuada? \n*Para sair, digite 's'*"); print ("\n")
    tab = input ()
    if tab == "s":
        msg_adeus()
        break
    while tab.isalpha() == True:
        print ("\n"); print ("*Entre com um número inteiro* \nQual será o número para a tabuada? \n*Para sair, digite 's'*"); print ("\n")
        tab = input ()
        if tab == "s":
            break
    if tab == "s":
        msg_adeus()
        break
    tab = float(tab)
    print ("\n")
    # Índice da tabuada:

    print ("Desejas ter a tabuada do", tab, "exibida a até qual número? \n*Para sair, digite 's'*"); print ("\n")
    index = input()
    while index.isdigit() == False:
        print ("\n"); print ("*Entre com um número inteiro* \nDesejas ter a tabuada do", tab, "exibida a até qual número? \n*Para sair, digite 's'*"); print ("\n")
        index = input ()
        if index == "s":
            break
    if index == "s":
        msg_adeus()
        break
    index = int(index) + 1
    # Resultado:

    print ("Tabuada do", tab, "de 1 até", index,":"); print ("\n")
    for index in range (1, index):
        print (tab,"*",index,"=", tab * index)
    print ("\n")
    # Loop:

    print ("Pressione 'Enter' para continuar \nPara sair, digite 's'"); print ("\n")
    tab = input ()
    if tab == "s":
        msg_adeus()
        break
    print ("\n")