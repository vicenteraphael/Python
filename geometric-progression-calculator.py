"""
Variáveis e Funções:
a = 1º termo (a1); termo anterior (an - 1)
b = índice do termo desejado (n de an); termo qualquer (an)
n = variável resposta; razão (n) da progressão

"""
a = 0
b = 0
n = 0
def menu():
    print ("Desejas encontrar:"); print ("\n")
    print ("1) Um termo n da progressão (an) \n2) A razão da progressão (q) \n3) A soma geral FINITA dos termos da progressão (Sn) \n4) A soma geral INFINITA dos termos da progressão \n5) Sair ")
    print ("\n")

def msg_adeus():
    print ("\n")
    print ("Adeus!")
print ("\n")

def voltar_sair():
    print ("\n")
    print ("Desejas:"); print ("\n")
    print ("1) Voltar ao Menu de opções \n2) Sair"); print ("\n")

# Boas vindas:

print ("Bem-vindo à Calculadora de Progressão Geométrica do Raphael"); print ("\n")
print ("Para continuar, pressione 'Enter' \nPara sair, digite 's'"); print ("\n")
n = input ()
if n == "s":
    msg_adeus()

# Menu de opções:

while n != "s":

    print ("\n"); menu()
    n = input ()
    while n != "1" and n != "2" and n != "3" and n != "4" and n != "5":
        print ("*alternativa inválida*"); menu(); n = input ()
    # Sair:

    if n == "5":
        msg_adeus()
        break

    # Termo Geral da Progressão (an):

    elif n == "1":

        # Entrada:

        print ("\n")
        print (" *para sair, entre com 's'* \nPara voltar ao Menu de opções, entre com 'm'"); print ("Informe-me:")
        while True:
            try:        
                a = input ("1º termo da progressão (a1): ")
                if a == "s":
                    break
                elif a == "m":                
                    break
                else:
                    a = float(a)
                    break
            except ValueError or TypeError:
                print ("Entre com números!")
                if a == "s":
                    break
        if a == "s":
            msg_adeus()
            break
        elif a == "m":
            continue
        while a != "m":
            while True:
                try:
                    b = input ("Índice do termo desejado (n de an): ")
                    if b == "s":
                        break
                    elif b == "m":
                        break
                    else:
                        b = float(b)
                        break
                except ValueError or TypeError:
                    print ("Entre com números!")
                    if b == "s":
                        break
            if b == "s":
                msg_adeus()
                break
            elif b == "m":
                continue
        while b != "m":
            while True:
                try:
                    n = input ("Razão da progressão (q): ")
                    if n == "s":
                        break
                    else:
                        n = float(n)
                        break
                except ValueError or TypeError:
                    print ("Entre com números!")
                    if n == "s":
                        break
            if n == "s":
                msg_adeus()
                break
            if n == "m":
                continue
        while n != "m":
            # Saída:

            print ("\n")
            print ("an =", a * n ** (b-1) )

        # Voltar ou Sair:

        voltar_sair()
        n = input ()
        if n == "2":
            msg_adeus()
            break

    # Razão da progressão (q):

    elif n == "2":

        # Entrada:
        print ("\n")
        print ("*para sair, entre com 's'* \nInforme-me dois termos consecutivos: "); print ("\n")
        while True:
            try:        
                b = input ("1º termo da progressão (an): ")
                if b == "s":
                    break
                elif b == "m":
                    break
                else:
                    b = float(b)
                    break
            except ValueError or TypeError:
                print ("Entre com números!")
                if b == "s":
                    break
        if b == "s":
            msg_adeus()
            break
        elif b == "m":
            continue
        if b != "m":
            while True:
                try:        
                    a = input ("Termo anterior (an - 1): ")
                    if a == "s":
                        break
                    elif a == "m":
                        break
                    else:
                        a = float(a)
                        break
                except ValueError or TypeError:
                    print ("Entre com números!")
                    if a == "s":
                        break
                    elif a == "m":
                        break
            if a == "s":
                msg_adeus()
                break
            if a == "m":
                continue
        if a != "m":
            # Saída:

            print ("\n")
            print ("q =", b / a)

            # Voltar ou Sair:

            voltar_sair()
            n = input ()
            if n == "2":
                msg_adeus()
                break
    
    # Soma geral FINITA dos termos da progressão (Sn):

    elif n == "3":
        
        # Entrada:

        print ("\n")
        print ("*para sair, entre com 's'* \nInforme-me"); print ("\n")
        while True:
            try:        
                a = input ("1º termo da progressão (a1): ")
                if a == "s":
                    break
                if a == "m":
                    break
                else:
                    a = float(a)
                    break
            except ValueError or TypeError:
                print ("Entre com números!")
                if a == "s":
                    break
        if a == "s":
            msg_adeus()
            break
        if a == "m":
            continue
        while a != "m":
            while True:
                try:
                    b = input ("Razão da progressão (q): ")
                    if b == "s":
                        break
                    else:
                        b = float(b)
                        break
                except ValueError or TypeError:
                    print ("Entre com números!")
                    if b == "s":
                        break
            if b == "s":
                msg_adeus
                break
            if b == "m":
                break
        while b != "m":
            while True:
                try:
                    n = input ("Quantidade de termos (n) da progressão: ")
                    if n == "s":
                        break
                    else:
                        n = float(n)
                        break
                except ValueError or TypeError:
                    print ("Entre com números!")
                    if n == "s":
                        break
            if n == "s":
                msg_adeus
                break
            if n == "m":
                continue
        while n != "m":
            # Saída:

            print ("\n")
            print ("Sn =", (a * (b ** n - 1)) / b - 1)

        # Voltar ou Sair:

        voltar_sair()
        n = input ()
        if n == "2":
            msg_adeus()
            break

    # Soma geral FINITA dos termos da progressão (Sn):

    elif n == "4":

        # Entrada:

        print ("\n")
        print ("*para sair, entre com 's'* \nInforme-me"); print ("\n")
        while True:
            try:        
                a = input ("1º termo da progressão (a1): ")
                if a == "s":
                    break
                elif a == "m":
                    break
                else:
                    a = float(a)
                    break
            except ValueError or TypeError:
                print ("Entre com números!")
                if a == "s":
                    break
        if a == "s":
            msg_adeus()
            break
        elif a == "m":
            continue
        while a != "m":
            while True:
                try:
                    b = input ("Razão da progressão (q): ")
                    if b == "s":
                        break
                    else:
                        b = float(b)
                        break
                except ValueError or TypeError:
                    print ("Entre com números!")
                    if b == "s":
                        break
            if b == "s":
                msg_adeus()
                break
            if b == "m":
                continue
        while b != "m":
            # Saída:

            print ("\n")
            print ("s∞ =", a / 1 - b)

        # Voltar ou Sair:

        voltar_sair()
        n = input ()
        if n == "2":
            msg_adeus()
            break