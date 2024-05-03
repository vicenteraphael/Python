def msg_erro():
    print ("\n")
    print ("*entre com números*"); print ("\n")
def msg_adeus():
    print ("\n")
    print ("Adeus")
def angulo():
    print ("\n")
    print ("Desejas ter Seno, Cosseno e Tangente referentes a qual ângulo? \n*para sair, digite 's'*"); print ("\n")
    print ("1) Alfa \n2) Beta"); print ("\n")
print ("\n")
print ("Bem-vindo ao Avaliador de Triângulos do Raphael"); print ("\n")
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
    #Cálculo:

    if a < b + c or b < a + c or c < a + b:    
        if a == b and b == c:
            print ("O Triângulo é Equilátero")
        elif a == b or b == c or b == a:
            print ("O Triângulo é Isósceles")
        elif a != b and b != c and a != c:
            print ("O Triângulo é Escaleno")
        if a**2 == b**2 + c**2 or b**2 == a**2 + c**2 or c**2 == b**2 + a**2:
            print ("O triângulo é Retângulo"); print ("\n")
        # Cálculo para Triângulo Retângulo:
            if a > b and a > c and b > c:
                hip = a
                catma = b
                catme= c
            elif a > b and a > c and c > b:
                hip = a
                catma = c
                catme= b
            elif b > a and b > c and a > c:
                hip = b
                catma = a
                catme = c
            elif b > a and b > c and c > a:
                hip = b
                catma = c
                catme = a
            elif c > a and c > b and a > b:
                hip = c
                catma = a
                catme = b
            elif c > a and c > b and b > a:
                hip = c
                catma = b
                catme = a
            print ("\nTendo Alfa como sendo o ângulo entre a hipotenusa o cateto menor\n e Beta como sendo o ângulo entre a hipotenusa e o maior cateto"); print ("\n")
            print ("Entre com o valor dos ângulos:"); print ("\n")
            A = input ("Alfa: ")
            while A.isalpha == True:
                msg_erro()
                A = input ()
                if A == "s":
                    break
            if A == "s":
                msg_adeus()
                break
            A = float(A)
            B = input ("Beta: ")
            while B.isalpha == True:
                msg_erro()
                B = input ()
                if B == "s":
                    break
            if B == "s":
                msg_adeus()
                break
            sina = catma / hip
            cosa = catme / hip
            tga = catma / catme
            sinb = catme / hip
            cosb = catma / hip
            tgb = catme / catma
            r = ""
            while r != "s":
                angulo()
                r = input ()
                while r != "1" and r != "2":
                    print ("*alternativa inválida*")
                    angulo()
                    r = input (); print ("\n")
                    if r == "s":
                        break
                if r == "s":
                    print ("Adeus!")
                    break
                if r == "1":
                    print ("seno de Alfa =", sina, "cosseno de Alfa =", cosa, "tangente de Alfa =", tga)
                elif r == "2":
                    print ("seno de Alfa =", sinb, "cosseno de Alfa =", cosb, "tangente de Alfa =", tgb)       
    else:
        print ("Os valores dados não formam um triângulo")
    print ("\n")