print ("\nBem-vindo(a) ao Programa Conversor do Raphael")
a = ""

# Menu de opções:

while a != "s":
    print ("\nDesejas converter: \n\n1) Decimal \n2) Binário \n3) Octal \n4) Hexadecimal \n5) Sair\n")
    a = input()
    while a != "1" and a != "2" and a != "3" and a != "4" and a != "5":
        print ("*Opção inválida*")
        print ("Desejas converter: \n\n1) Decimal \n2) Binário \n3) Octal \n4) Hexadecimal \n5) Sair\n")
        a = input()
    if a == "5":
        break
    elif a == "1":
        print ("\nPara: \n\n2) Binário \n3) Octal \n4) Hexadecimal \n5) Sair \n6) Voltar ao menu de opções \n")
        b = input()
        while b != "2" and b != "3" and b != "4" and b != "5" and b != "6":
            print ("*Opção inválida*")
            print ("Para: \n\n2) Binário \n3) Octal \n4) Hexadecimal \n5) Sair \n6) Voltar ao menu de opções \n")
            b = input()
    elif a == "2":
        print ("\nPara: \n\n1) Decimal \n3) Octal \n4) Hexadecimal \n5) Sair \n6) Voltar ao menu de opções \n")
        b = input()
        while b != "1" and b != "3" and b != "4" and b != "5" and b != "6":
            print ("*Opção inválida*")
            print ("Para: \n\n1) Decimal \n3) Octal \n4) Hexadecimal \n5) Sair \n6) Voltar ao menu de opções \n")
            b = input()
    elif a == "3":
        print ("\nPara: \n\n1) Decimal \n2) Binário \n4) Hexadecimal \n5) Sair \n6) Voltar ao menu de opções \n")
        b = input()
        while b != "1" and b != "2" and b != "4" and b != "5" and b != "6":
            print ("*Opção inválida*")
            print ("Para: \n\n1) Decimal \n2) Binário \n4) Hexadecimal \n5) Sair \n6) Voltar ao menu de opções \n")
            b = input()
    else:
        print ("\nPara: \n\n1) Decimal \n2) Binário \n3) Octal \n5) Sair \n6) Voltar ao menu de opções \n")
        b = input()
        while b != "1" and b != "2" and b != "3" and b != "5" and b != "6":
            print ("*Opção inválida*")
            print ("Para: \n\n1) Decimal \n2) Binário \n3) Octal \n5) Sair \n6) Voltar ao menu de opções \n")
            b = input()

    if b == "5":
        break

    # Decimal para Binário:

    while a == "1" and b == "2":
        while True:
            try:
                a = input ("Nº: ")
                if a == "s" or a == "m":
                    break
                a = int(a)
                break
            except:
                print ("Entre com um número!")
        if a == "s":
            break
        print (a ,"=", format(a, "b"))


    # Decimal para Octal:

    # Decimal para Hexadecimal:

    # Binário para Decimal:

    # Binário para Octal:

    # Binário para Hexadecimal:

    # Octal para Decimal:

    # Octal para Binário:

    # Octal para Hexadecimal:

    # Hexadecimal para Decimal:

    # Hexadecimal para Binário:

    # Hexadecimal para Octal:

print ("\nAdeus!")