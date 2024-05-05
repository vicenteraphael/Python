def msg_adeus():
    print ("\n"); print ("Adeus!")

a = ""
b = ""
c = ""

print ("\n\nBem-vindo à Calculadora de Juros Simples do Raphael")

# Menu de opções:

while a != "s" and b != "s" and c != "s" and b != "3":
    a = ""
    b = ""
    c = ""
    print ("\n\nDesejas calcular: \n\n1) Juros (J) e Montante (M) \n2) Capital (C) \n3) Taxa em meses (i) \n4) Tempo (t) \n5) Sair \n\n")
    a = input ()
    while a != "1" and a != "2" and a != "3" and a != "4":
        print ("\n\n*alternativa inválida*")
        print ("\n\nDesejas calcular: \n\n1) Juros e Montante \n2) Capital (C) \n3) Taxa \n4) Tempo \n5) Sair\n\n")
        a = input ()
    if a == "5":
        msg_adeus()

    # Juros e Montante:

    while a == "1":
        print ("\n\n*Para sair, entre com 's' \nPara voltar ao Menu de Opções, entre com 'm'* \n\nInforme-me:"); print ("\n")
        while True:
            try:
                a = input ("Capital (C): ")
                if a == "s" or a == "m":
                    break
                else:
                    a = float(a)
                    break
            except ValueError or TypeError:
                print ("Entre com um número!")
        if a == "s":
            msg_adeus()
            break
        elif a != "m":
            while True:
                try:
                    b = input ("Taxa em meses (i): ")
                    if b == "s" or b == "m":
                        break
                    else:
                        b = float(b)
                        break
                except ValueError or TypeError:
                    print ("Entre com um número!")
            if b == "s":
                msg_adeus()
                break
        if a != "m" and  b != "m":
            while True:
                try:
                    c = input ("Tempo (t): ")
                    if c == "s" or c == "m":
                        break
                    else:
                        c = float(c)
                        break
                except ValueError or TypeError:
                    print ("Entre com um número!")
            if c == "s":
                msg_adeus()
                break

        # Cálculo/Resultado:

        if a != "m" and b != "m" and c != "m":
            c = (a * b * c)/100
            a = a + c
            print ("J =", c, "\nM =", a)
            
            # Voltar, Continuar ou Sair:

            print ("\n\nDesejas: \n\n1) Continuar \n2) Voltar ao Menu de opções \n3) Sair \n\n")
            b = input ()
            while b != "1" and b != "2" and b != "3":
                print ("\n\n*alternativa inválida*\nDesejas: \n\n1) Continuar \n2) Voltar ao Menu de opções \n3) Sair")
                b = input ()
                if b == "3":
                    break
            if b == "3":
                msg_adeus()
                break
            elif b == "2":
                break
            elif b == "1":
                a = "1"

    # Capital:

    while a == "2":
        print ("\n*para sair, entre com 's' \npara voltar ao Menu de opções, entre com 'm'*\nVocê sabe o valor de(o): \n\n1) Juros (J), Taxa (i), Tempo (t)  \n2) Montante \n\n")
        a = input ("")
        while a != "1" and a != "2" and a != "s" and a != "m":
            print ("\n*alternativa inválida*\n*para sair, entre com 's' \npara voltar ao Menu de opções, entre com 'm'*\nVocê sabe o valor de(o): \n\n1) Juros (J), Taxa (i), Tempo (t)  \n2) Montante \n\n")
            a = input ("")
            if a == "s" or a == "m":
                break
        if a == "s":
            msg_adeus()
        elif a == "m":
            break
        elif a == "1":
            print ("\n\n*para sair, entre com 's' \npara voltar ao Menu de opções, entre com 'm'*Informe-me: \n\n")
            while True:
                try:
                    a = input ("Juros (J): ")
                    if a == "s" or a == "m":
                        break
                    else:
                        a = float(a)
                        break
                except ValueError or TypeError:
                    print ("Entre com um número!")
            if a == "s":
                msg_adeus()
                break
            if a == "1":
                while True:
                    try:
                        b = input ("Tempo (t): ")
                        if b == "s" or b == "m":
                            break
                        else:
                            b = float(b)
                            break
                    except ValueError or TypeError:
                        print ("Entre com um número!")
                if b == "s":
                    msg_adeus()
                    break
            if a != "m" and b != "m":
                while True:
                    try:
                        c = input ("Tempo (t): ")
                        if c == "s" or c == "m":
                            break
                        else:
                            c = float(c)
                            break
                    except ValueError or TypeError:
                        print ("Entre com um número!")
                if c == "s":
                    msg_adeus()
                    break
            if a != "m" and b != "m" and c != "m":

                # Cálculo/Resultado:

                print ("Capital =", (100 * a) / (b * c))
