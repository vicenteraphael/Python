def msg_erro():
    print ("\n")
    print ("*entre com números*"); print ("\n")
def msg_adeus():
    print ("\n")
    print ("Adeus")
print ("\n")
print ("Bem-vindo ao Avaliador de Triângulos do Raphael"); print ("\n")
print ("Pressione 'Enter' para continuar \nPara sair, digite 's'"); print ("\n")
a = input ()
if a == "s":
    msg_adeus()
while a != "s":
    #Valores de Entrada:

    print ("Entre com os valores do Triângulo: \n*Para sair, digite 's'*"); print ("\n")
    a = input ("1º lado: ")
    while a.isalpha == True:
        msg_erro()
        a = input ()
        if a == "s":
            break
    if a == "s":
        msg_adeus()
        break
    a = float(a)
    b = input ("2º lado: ")
    while b.isalpha == True:
        msg_erro()
        b = input ()
        if b == "s":
            break
    if b == "s":
        msg_adeus()
        break
    b = float(b)
    c = input ("3º lado: ")
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
        
            print ("Entre com o valor dos ângulos: ")
            a = input ("1º ângulo: ")
            while a.isalpha == True:
                msg_erro()
                a = input ()
                if a == "s":
                    break
            if a == "s":
                msg_adeus()
                break
            a = float(a)
            b = input ("2º ângulo: ")
            while b.isalpha == True:
                msg_erro()
                b = input ()
                if b == "s":
                    break
            if b == "s":
                msg_adeus()
                break
            b = float(b)
            c = input ("3º ângulo: ")
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
    else:
        print ("Os valores dados não formam um triângulo")
    print ("\n")