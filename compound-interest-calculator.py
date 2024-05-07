def msg_adeus():
    print ("\n\nAdeus!")

print ("\nBem-vindo(a) à Calculadora de Juros Compostos do Raphael\n")

# Menu de opções:

a = ""
b = ""
c = ""

while a != "s" and b != "s" and b != "3" and c != "s":
    a = ""
    b = ""
    c = ""
    print ("\nDesejas calcular: \n\n1) Juros (J) e Montante (M) \n2) Capital (C) \n3) Taxa percentual (i) \n4) Tempo em meses (t) \n5) Sair\n")
    a = input ()
    while a != "1" and a != "2" and a != "3" and a != "4" and a != "5":
        print ("\n*alternativa inválida*\n\nDesejas calcular:\n \n1) Juros (J) e Montante (M) \n2) Capital (C) \n3) Taxa percentual (i) \n4) Tempo em meses (t) \n5) Sair\n")
        a = input ()
    if a == "5":
        msg_adeus()
        break

    # Juros (J) e Montante (M):

    while a == "1":
        print ("\n*para sair, entre com 's' \npara voltar ao Menu de opções, entre com 'm'* \n\nInforme-me:\n")
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
                    b = input ("Taxa percentual (i): ")
                    if b == "s" or b == "m":
                        break
                    else:
                        b = float(b)
                        break
                except ValueError or TypeError:
                    print ("Entre com un número!")
            if b == "s":
                msg_adeus()
                break
            elif a != "m" and b != "m":
                while True:
                    try:
                        c = input ("Tempo em meses (t): ")
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
                elif a != "m" and b != "m" and c != "m":

                    # Cálculo/Resultado:

                    print ("\nM =", a * (b + 1) ** c, "\nJ =", (a * (b + 1) ** c ) - a)

                    # Continuar/Voltar/Sair

                    print ("\nDesejas: \n\n1) Continuar \n2) Voltar ao Menu de opções \n3) Sair\n")
                    b = input ()
                    while b != "1" and b != "2" and b != "3":
                        print ("\n*alternativa inválida*\nDesejas: \n\n1) Continuar \n2) Voltar \n3) Sair\n")
                        b = input ()
                    if b == "3":
                        msg_adeus()
                        break
                    elif b == "2":
                        break
                    elif b == "1":
                        a = "1"
    
    # Capital (C):
    
    while a == "2":
        print ("\n*para sair, entre com 's' \npara voltar ao Menu de opções, entre com 'm'*\n\nVocê prefere calcular a partir de: \n\n1) Montante (M), Taxa percentual (i), Tempo em meses (t) \n2) Juros (J), Taxa percentual (i), Tempo em meses(t) \n3) Montante (M) e Juros (J)\n\n")
        b = input ()
        while b != "1" and b != "2" and b != "3" and b != "s" and b != "m":
            print ("\n*alternativa inválida*\n*para sair, entre com 's' \npara voltar ao Menu de opções, entre com 'm'*\n\nVocê prefere calcular a partir de: \n\n1) Montante (M), Taxa percentual (i), Tempo em meses (t) \n2) Montante (M) e Juros (J)\n\n")
            b = input ()
        if b == "s":
            msg_adeus()
            break
        elif b == "m":
            break
        elif b == "1":
            print ("\n*para sair, entre com 's' \npara voltar ao Menu de opções, entre com 'm'* \n\nInforme-me:\n")
            while True:
                try:
                    a = input("Montante (M): ")
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
                        b = input ("Taxa percentual (i): ")
                        if b == "s" or b == "a":
                            break
                        else:
                            b = float(b)
                            break
                    except ValueError or TypeError:
                        print ("Entre com um número!")
                if b == "s":
                    msg_adeus()
                    break
                elif a != "m" and b != "m":
                    while True:
                        try:
                            c = input ("Tempo em meses (t): ")
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
                    elif a != "m" and b != "m" and c != "m":

                        # Cálculo/Resultado:

                        print ("\nC =", a / (1 + b) ** c)

                        # Continuar/Voltar/Sair:

                        print ("\nDesejas: \n\n1) Continuar \n2) Voltar ao Menu de opções \n3) Sair\n")
                        b = input ()
                        while b != "1" and b != "2" and b != "3":
                            print ("\na*lternativa inválida*\nDesejas: \n\n1) Continuar \n2) Voltar \n3) Sair\n")
                            b = input ()
                        if b == "3":
                            msg_adeus()
                            break
                        elif b == "2":
                            break
                        elif b == "1":
                            a = "2"
        elif b == "2":
            print ("\n*para sair, entre com 's' \npara voltar ao Menu de opções, entre com 'm'* \n\nInforme-me:\n")
            while True:
                try:
                    a = input("Juros (J): ")
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
                        b = input ("Taxa percentual (i): ")
                        if b == "s" or b == "a":
                            break
                        else:
                            b = float(b)
                            break
                    except ValueError or TypeError:
                        print ("Entre com um número!")
                if b == "s":
                    msg_adeus()
                    break
                elif a != "m" and b != "m":
                    while True:
                        try:
                            c = input ("Tempo em meses (t): ")
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
                    elif a != "m" and b != "m" and c != "m":

                        # Cálculo/Resultado:

                        print ("\nC =", a / (((1 + b) ** c) - 1))

                        # Continuar/Voltar/Sair:

                        print ("\nDesejas: \n\n1) Continuar \n2) Voltar ao Menu de opções \n3) Sair\n")
                        b = input ()
                        while b != "1" and b != "2" and b != "3":
                            print ("\n*alternativa inválida*\nDesejas: \n\n1) Continuar \n2) Voltar \n3) Sair\n")
                            b = input ()
                        if b == "3":
                            msg_adeus()
                            break
                        elif b == "2":
                            break
                        elif b == "1":
                            a = "2"
        elif b == "3":
            print ("\n*para sair, entre com 's' \npara voltar ao Menu de opções, entre com 'm'* \n\nInforme-me:\n")
            while True:
                try:
                    a = input("Montante (M): ")
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
                        b = input ("Juros (J): ")
                        if b == "s" or b == "a":
                            break
                        else:
                            b = float(b)
                            break
                    except ValueError or TypeError:
                        print ("Entre com um número!")
                if b == "s":
                    msg_adeus()
                    break
                elif a != "m" and b != "m":

                    # Cálculo/Resultado:

                    print ("\nC =", a - b)

                    # Continuar/Voltar/Sair:

                    print ("\nDesejas: \n\n1) Continuar \n2) Voltar ao Menu de opções \n3) Sair\n")
                    b = input ()
                    while b != "1" and b != "2" and b != "3":
                        print ("\na*lternativa inválida*\nDesejas: \n\n1) Continuar \n2) Voltar \n3) Sair\n")
                        b = input ()
                    if b == "3":
                        msg_adeus()
                        break
                    elif b == "2":
                        break
                    elif b == "1":
                        a = "2"

    # Taxa percentual (i):

    while a == "3":
        print ("\n*para sair, entre com 's' \npara voltar ao Menu de opções, entre com 'm'* \n\nInforme-me:\n")
        while True:
            try:
                a = input ("Montante (M): ")
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
                    b = input ("Capital (C): ")
                    if b == "s" or b == "m":
                        break
                    else:
                        b = float(b)
                        break
                except ValueError or TypeError:
                    print ("Entre com un número!")
            if b == "s":
                msg_adeus()
                break
            elif a != "m" and b != "m":
                while True:
                    try:
                        c = input ("Tempo em meses (t): ")
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
                elif a != "m" and b != "m" and c != "m":

                    # Cálculo/Resultado:

                    print ("\ni =", (a / b) ** (1 / c) - 1, "%")

                    # Continuar/Voltar/Sair

                    print ("\nDesejas: \n\n1) Continuar \n2) Voltar ao Menu de opções \n3) Sair\n")
                    b = input ()
                    while b != "1" and b != "2" and b != "3":
                        print ("\n*alternativa inválida*\n\nDesejas: \n\n1) Continuar \n2) Voltar \n3) Sair\n")
                        b = input ()
                    if b == "3":
                        msg_adeus()
                        break
                    elif b == "2":
                        break
                    elif b == "1":
                        a = "3"
    
    # Tempo em meses (t)

    while a == "4":
        print ("\n*para sair, entre com 's' \npara voltar ao Menu de opções, entre com 'm'* \n\nInforme-me:\n")
        while True:
            try:
                a = input ("Montante (M): ")
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
                    b = input ("Capital (C): ")
                    if b == "s" or b == "m":
                        break
                    else:
                        b = float(b)
                        break
                except ValueError or TypeError:
                    print ("Entre com un número!")
            if b == "s":
                msg_adeus()
                break
            elif a != "m" and b != "m":
                while True:
                    try:
                        c = input ("Taxa percentual (i): ")
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
                elif a != "m" and b != "m" and c != "m":

                    # Cálculo/Resultado:
                    
                    a /= b
                    b = 0
                    c += 1
                    n = c
                    while c <= a:
                        b += 1
                        c *= n
                    if c % a != 0:
                        b += 1
                    print ("\nt =", b, "mes(es)")

                    # Continuar/Voltar/Sair

                    print ("\nDesejas: \n\n1) Continuar \n2) Voltar ao Menu de opções \n3) Sair\n")
                    b = input ()
                    while b != "1" and b != "2" and b != "3":
                        print ("\na*lternativa inválida*\nDesejas: \n\n1) Continuar \n2) Voltar \n3) Sair\n")
                        b = input ()
                    if b == "3":
                        msg_adeus()
                        break
                    elif b == "2":
                        break
                    elif b == "1":
                        a = "4"