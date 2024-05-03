def msg_erro():
    print ("\n")
    print ("*entre com números*"); print ("\n")
def msg_adeus():
    print ("\n")
    print ("Adeus!")
print ("\n")
print ("Bem-vindo à Calculadora Trigonométrica do Raphael"); print ("\n")
print ("Pressione 'Enter' para continuar \nPara sair, digite 's'"); print ("\n")
a = input ()
if a == "s":
    msg_adeus()
while a != "s":
    #Valores de Entrada:

    print ("Entre com os valores do Triângulo: \n*Para sair, digite 's'*"); print ("\n")
    a = input ("1º lado (a): ")
    while a.isalpha == True:
        msg_erro()
        a = input ()
        if a == "s":
            break
    if a == "s":
        msg_adeus()
        break
    a = float(a)
    b = input ("2º lado (b): ")
    while b.isalpha == True:
        msg_erro()
        b = input ()
        if b == "s":
            break
    if b == "s":
        msg_adeus()
        break
    b = float(b)
    c = input ("3º lado (c): ")
    while c.isalpha == True:
        msg_erro()
        c = input ()
        if c == "s":
            break
    if c == "s":
        msg_adeus()
        break
    c = float(c)
    print ("\n")
    #Tipo de Triângulo:

    if a < b + c and b < a + c and c < a + b:    
        if a == b and b == c:
            print ("O Triângulo é Equilátero")
        elif a == b or b == c or b == a:
            print ("O Triângulo é Isósceles")
        elif a != b and b != c and a != c:
            print ("O Triângulo é Escaleno")
        if a**2 == b**2 + c**2 or b**2 == a**2 + c**2 or c**2 == b**2 + a**2:
            print ("O triângulo é Retângulo")
        print ("\n")
        print ("Desejas:"); print ("\n")
        print ("1) Voltar ao início \n2) Calcular Seno, Cosseno e Tangente \n3) Sair"); print ("\n")
        r = input (); print ("\n")
        if r != "1" and r != "2" and r != "3":
            print ("*alternativa inválida* Desejas:"); print ("\n")
            print ("1) Voltar ao início \n2) Calcular Seno, Cosseno e Tangente \n3) Sair"); print ("\n")
            r = input (); print ("\n")
        elif r == "3":
            print ("Adeus")
            break
        elif r == "2":
        # Cálculo Trigonométrico:

            print ("\nTendo Alfa como sendo o ângulo oposto ao lado a:", a ,"\n Beta sendo o ângulo oposto ao lado b:", b,"\ne Theta sendo o ângulo oposto ao lado c:", c,); print ("\n")
            cosa = (a**2 - (b**2 + c**2)) / (- 2 * b * c)
            sina = (1 - cosa**2) ** 0.5
            tga = sina / cosa
            cosb = (b**2 - (a**2 + c**2)) / (- 2 * a * c)
            sinb = (1 - cosb**2) ** 0.5
            tgb = sinb / cosb
            cosc = (c**2 - (a**2 + b**2)) / (- 2 * a * b)
            sinc = (1 - cosc**2) ** 0.5
            tgc = sinc / cosc
            print ("seno de Alfa =", sina, "      cosseno de Alfa =", cosa, "      tangente de Alfa =", tga)
            print ("seno de Beta =", sinb, "      cosseno de Beta =", cosb, "      tangente de Beta =", tgb)
            print ("seno de Theta =", sinc, "      cosseno de Theta =", cosc, "      tangente de Theta =", tgc); print ("\n")
            print ("Para continuar, pressione 'Enter' \nPara sair, digite 's'"); print ("\n")
            r = input ()
            if r == "s":
                msg_adeus()
                break
        elif r == "1":
            continue
    else:
        print ("Os valores dados não formam um triângulo :/"); print ("\n")
        print ("Para continuar, pressione 'Enter' \nPara sair, digite 's'"); print ("\n")
        r = input ()
        if r == "s":
            msg_adeus()
            break
    print ("\n")