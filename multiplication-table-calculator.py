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

    print ("*para sair, digite 's'* \nInforme-me:"); print ("\n")
    tab = input("Qual será o número para a tabuada: ")
    if tab == "s":
        msg_adeus()
        break
    while tab.isalpha() == True:
        print ("\n"); print ("*Entre com um número!* \nQual será o número para a tabuada? ")
        tab = input ()
        if tab == "s":
            break
    if tab == "s":
        msg_adeus()
        break
    tab = float(tab)
    # Índice da tabuada:

    index = input ("Qual será o índice da tabuada (multiplica-se do 1 até ...): ")
    if index == "s":
        msg_adeus()
        break
    while index.isdigit() == False:
        input ("\n")
        index = input ("Entre com um número inteiro! \nQual será o índice da tabuada?")
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
    # Loop:

    print ("Pressione 'Enter' para continuar \nPara sair, digite 's'"); print ("\n")
    tab = input ()
    if tab == "s":
        msg_adeus()
        break
    print ("\n")