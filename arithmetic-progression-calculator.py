def num_invalido():
    print ("\n")
    print ("*número inválido*")
def msg_adeus():
    print ("\n")
    print ("Adeus!")
print ("\n")
print ("Bem-vindo à Calculadora de Progressão Aritmética do Raphael"); print ("\n")
print ("Para inciar, pressione 'Enter' \nPara sair, digite 's'"); print ("\n")
n = input ()
if n == "s":
    msg_adeus()
while n != "s":
    print ("Você deseja encontrar:"); print ("\n")
    print ("1) Um termo n da progressão (an) \n2) A razão da progressão (r) \n3) A soma geral dos termos da progressão (Sn) \n4) Sair"); print ("\n")
    n = input ()
    while n != "1" and n != "2" and n != "3" and n != "4":
        print ("\n")
        print ("*alternativa inválida*")
        print ("Você deseja encontrar:"); print ("\n")
        print ("1) Um termo n da progressão (an) \n2) A razão da progressão (r) \n3) A soma geral dos termos da progressão (sn) \n4) Sair"); print ("\n")
        n = input ()
    if n == "4":
        msg_adeus()
        break
    elif n == "2":
        print ("\n")
        print ("Informe-me dois termos consecutivos da progressão: \n*para sair, digite 's'*"); print ("\n")
        a = input ("1º termo: ")
        if a == "s":
            msg_adeus()
            break
        while a.isalpha() == True:
            num_invalido()
            a = input ("1º termo: ")
            if a == "s":
                break
        if a == "s":
            msg_adeus()
            break
        a = float(a)
        b = input ("2º termo: ")
        if b == "s":
            msg_adeus()
            break
        while b.isalpha() == True:
            num_invalido()
            b = input ("2º termo")
            if b == "s":
                break
        if b == "s":
            msg_adeus()
            break
        b = float(b)
        print ("\n")
        print ("r =", b - a)
    elif n == "1":
        print ("\n")
        print ("*para sair, digite 's'* \nInforme-me:"); print ("\n")
        a = input ("1º termo da progressão (a1): ")
        if a == "s":
            msg_adeus()
            break
        while a.isalpha() == True:
            num_invalido()
            a = input ("1º termo da progressão (a1): ")
            if a == "s":
                break
        if a == "s":
            msg_adeus()
            break
        a = float(a)
        b = input ("A razão da progressão (r): ")
        if b == "s":
            msg_adeus()
            break
        while b.isalpha() == True:
            num_invalido()
            b = input ("A razão da progressão (r): ")
            if b == "s":
                break
        if b == "s":
            msg_adeus()
            break
        b = float(b)
        n = input ("O índice do termo desejado (n): ")
        if n == "s":
            msg_adeus()
            break
        while n.isalpha() == True:
            num_invalido()
            n = input ("O índice do termo desejado (n): ")
            if n == "s":
                break
        if n == "s":
            msg_adeus()
            break
        n = float(n)
        print ("\n")
        print ("an =", a + (n - 1) * b)
    elif n == "3":
        print ("\n")
        print ("*para sair, digite 's'* \nInforme-me:"); print ("\n")
        a = input ("1º termo da progressão (a1): ")
        if a == "s":
            msg_adeus()
            break
        while a.isalpha() == True:
            num_invalido()
            a = input ("1º termo da progressão (a1): ")
            if a == "s":
                break
        if a == "s":
            msg_adeus()
            break
        a = float(a)
        n = input ("O último termo da progressão (an): ")
        if n == "s":
            msg_adeus()
            break
        while n.isalpha() == True:
            num_invalido()
            n = input ("O último termo da progressão (an): ")
            if n == "s":
                break
        if n == "s":
            msg_adeus()
            break
        n = float(n)
        b = input ("Índice do último termo da progressão (n): ")
        if b == "s":
            msg_adeus()
            break
        while b.isalpha() == True:
            num_invalido()
            b = input ("Índice do último termo da progressão (n): ")
            if b == "s":
                break
        if b == "s":
            msg_adeus()
            break
        b = float(b)
        print ("\n")
        print ("Sn =", ((a + n) * b ) / 2)
    print ("\n")
    print ("Para voltar, pressione 'Enter' \nPara sair, entre com o número 4 ou com a letra 's'"); print ("\n")
    n = input ()
    if n == "4":
        msg_adeus()
        break
