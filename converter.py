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

    if a == "1" and b == "2":
        print ("*para sair, entre com 's'\npara voltar, entre com 'm'*\n\nDecimal para Binário:\n")
        while True:
            a = input ("Nº: ")
            if a == "s" or a == "m":
                break
            try:
                print (a ,"=", format(int(a), "b"), "\n")
            except:
                print ("\nEntre com um número de base decimal!")

    # Decimal para Octal:

    elif a == "1" and b == "3":
        print ("*para sair, entre com 's'\npara voltar, entre com 'm'*\n\nDecimal para Octal:\n")
        while True:
            a = input ("Nº: ")
            if a == "s" or a == "m":
                break
            try:
                print (a, "=", format(int(a), "o"), "\n")
            except:
                print ("\nEntre com um número de base decimal!")

    # Decimal para Hexadecimal:

    elif a == "1" and b == "4":
        print ("*para sair, entre com 's'\npara voltar, entre com 'm'*\n\nDecimal para Hexadecimal:\n")
        while True:
            a = input ("Nº: ")
            if a == "s" or a == "m":
                break
            try:
                print (a, "=", format(int(a), "X"), "\n")
            except:
                print ("\nEntre com um número de base decimal!")

    # Binário para Decimal:

    elif a == "2" and b == "1":
        print ("*para sair, entre com 's'\npara voltar, entre com 'm'*\n\nBinário para Decimal:\n")
        while True:
            a = input ("Nº: ")
            if a == "s" or a == "m":
                break
            try:
                print (a, "=", int(a, 2), "\n")
            except:
                print ("\nEntre com um número binário!")
    
    # Binário para Octal:

    elif a == "2" and b == "3":
        print ("*para sair, entre com 's'\npara voltar, entre com 'm'*\n\nBinário para Octal:\n")
        while True:
            a = input ("Nº: ")
            if a == "s" or a == "m":
                break
            try:
                print (a, "=", format(int(a, 2), "o"), "\n")
            except:
                print ("\nEntre com um número binário!")

    # Binário para Hexadecimal:

    elif a == "2" and b == "4":
        print ("*para sair, entre com 's'\npara voltar, entre com 'm'*\n\nBinário para Hexadecimal:\n")
        while True:
            a = input ("Nº: ")
            if a == "s" or a == "m":
                break
            try:
                print (a, "=", format(int(a, 2), "X"), "\n")
            except:
                print ("\nEntre com um número binário!")

    # Octal para Decimal:

    elif a == "3" and b == "1":
        print ("*para sair, entre com 's'\npara voltar, entre com 'm'*\n\nOctal para Decimal:\n")
        while True:
            a = input ("Nº: ")
            if a == "s" or a == "m":
                break
            try:
                print (a, "=", int(a, 8), "\n")
            except:
                print ("\nEntre com um número octal!")

    # Octal para Binário:
    
    elif a == "3" and b == "2":
        print ("*para sair, entre com 's'\npara voltar, entre com 'm'*\n\nOctal para Binário:\n")
        while True:
            a = input ("Nº: ")
            if a == "s" or a == "m":
                break
            try:
                print (a, "=", format(int(a, 8), "b"), "\n")
            except:
                print ("\nEntre com um número octal!")

    # Octal para Hexadecimal:

    elif a == "3" and b == "4":
        print ("*para sair, entre com 's'\npara voltar, entre com 'm'*\n\nOctal para Hexadecimal:\n")
        while True:
            a = input ("Nº: ")
            if a == "s" or a == "m":
                break
            try:
                print (a, "=", format(int(a, 8), "X"), "\n")
            except:
                print ("\nEntre com um número octal!")

    # Hexadecimal para Decimal:

    elif a == "4" and b == "1":
        print ("*para sair, entre com 's'\npara voltar, entre com 'm'*\n\nHexadecimal para Decimal:\n")
        while True:
            a = input ("Nº: ")
            if a == "s" or a == "m":
                break
            try:
                print (a, "=", int(a, 16), "\n")
            except:
                print ("\nEntre com um número hexadecimal!")

    # Hexadecimal para Binário:

    elif a == "4" and b == "2":
        print ("*para sair, entre com 's'\npara voltar, entre com 'm'*\n\nHexadecimal para Decimal:\n")
        while True:
            a = input ("Nº: ")
            if a == "s" or a == "m":
                break
            try:
                print (a, "=", format(int(a, 16), "b"), "\n")
            except:
                print ("\nEntre com um número hexadecimal!")

    # Hexadecimal para Octal:

    elif a == "4" and b == "3":
        print ("*para sair, entre com 's'\npara voltar, entre com 'm'*\n\nHexadecimal para Octal:\n")
        while True:
            a = input ("Nº: ")
            if a == "s" or a == "m":
                break
            try:
                print (a, "=", format(int(a, 16), "o"), "\n")
            except:
                print ("\nEntre com um número hexadecimal!")

print ("\nAdeus!")