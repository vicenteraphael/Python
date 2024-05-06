def msg_adeus():
    print ("\n\nAdeus!")

print ("Bem-vindo à Calculadora de Juros Compostos do Raphael\n\n")

# Menu de opções:
a = ""
b = ""
c = ""
while a != "s" and b != "s" and b != "3" and c != "s":
    a = ""
    b = ""
    c = ""
    print ("\nDesejas calcular: \n\n1) Juros (J) e Montante (M) \n2) Capital (C) \n3) Taxa percentual (i) \n4) Tempo em meses (i) \n5) Sair\n")
    a = input ()
    while a != "1" and a != "2" and a != "3" and a != "4" and a != "5":
        print ("*alternativa inválida\nDesejas calcular: \n1) Juros (J) e Montante (M) \n2) Capital (C) \n3) Taxa percentual (i) \n4) Tempo em meses (i) \n5) Sair\n")
        a = input ()
    if a == "5":
        msg_adeus()
        break

    # Juros (J) e Montante (M):

    while a == "1":
        print ("\nInforme-me\n")
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
                        print ("\na*lternativa inválida*\nDesejas: \n\n1) Continuar \n2) Voltar \n3) Sair\n")
                        b = input ()
                    if b == "3":
                        msg_adeus()
                        break
                    elif b == "2":
                        break
                    elif b == "1":
                        a = "1"