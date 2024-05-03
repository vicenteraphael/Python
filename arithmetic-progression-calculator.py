def num_invalido():
    print ("\n")
    print ("*número inválido*")
def msg_adeus():
    print ("\n")
    print ("Adeus!")
print ("\n")
print ("Bem-vindo à Calculadora de Progressão Aritmética do Raphael"); print ("\n")
print ("Para inciar, pressione 'Enter' \nPara sair, digite 's'")
n = input ()
if n == "s":
    msg_adeus()
while n != "s":
    print ("Você deseja encontrar:"); print ("\n")
    print ("1) Um termo n da progressão \n2) A razão da progressão \n3) A soma geral dos termos da progressão \n4) Sair"); print ("\n")
    n = input ()
    while n != "1" and n != "2" and n != "3" and n != "4":
        print ("*alternativa inválida*")
        print ("Você deseja encontrar:"); print ("\n")
        print ("1) Um termo n da progressão (an) \n2) A razão da progressão (r) \n3) A soma geral dos termos da progressão (sn) \n4) Sair"); print ("\n")
        n = input ()
    if n == "4":
        msg_adeus()
        break
    elif n == "2":
        print ("Informe-me dois termos consecutivos da progressão \n*para sair, digite 's'*"); print ("\n")
        a = input ("1º termo")
        while a.isalpha() == True:
            num_invalido()
            a = input ("1º termo: ")
            if a == "s":
                break
        if a == "s":
            break
        a = float(a)
        b = input ("2º termo: ")
        while b.isalpha() == True:
            num_invalido()
            b = input ("2º termo")
            if b == "s":
                break
        if b == "s":
            break
        b = float(b)
        print ("r =", a - b)
    elif n == "1":
        print ("Informe-me:"); print ("\n")
        a = input ("1º termo da progressão (a1): ")
        while a.isalpha() == True:
            num_invalido()
            a = input ("1º termo da progressão (a1): ")
            if a == "s":
                break
        if a == "s":
            break
        a = float(a)
        b = input ("a razão da progressão (r): ")
        while b.isalpha() == True:
            num_invalido()
            b = input ("a razão da progressão (r): ")
            if b == "s":
                break
        if b == "s":
            break
        b = float(b)
        an = input ("O termo desejado (an): ")
        while an.isalpha() == True:
            num_invalido()
            an = input ("O termo desejado (an): ")
            if an == "s":
                break
        if an == "s":
            break
        an = float(an)
        print ("an =", a + (an - 1) * b)