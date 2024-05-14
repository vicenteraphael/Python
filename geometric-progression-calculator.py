"""
Variáveis e Funções:
a = 1º termo (a1); termo anterior (an - 1); variável resposta
b = índice do termo desejado (n de an); termo qualquer (an)
n = variável resposta; razão (n) da progressão

"""

a = ""
b = ""
n = ""

def informe():
    print ("\n*Para sair, entre com 's' \nPara voltar ao menu de opções, entre com 'm'* \n\nInforme: \n\n")

def menu():
    print ("Desejas encontrar:"); print ("\n")
    print ("1) Um termo n da progressão (an) \n2) A razão da progressão (q) \n3) A soma geral FINITA dos termos da progressão (Sn) \n4) A soma geral INFINITA dos termos da progressão (s∞) \n5) Sair ")
    print ("\n")

def msg_adeus():
    print ("\n")
    print ("Adeus!")
print ("\n")

def voltar_sair():
    print ("\n")
    print ("Desejas:"); print ("\n")
    print ("1) Continuar \n2) Voltar ao Menu de opções \n3) Sair"); print ("\n")

# Boas vindas:

print ("\nBem-vindo(a) à Calculadora de Progressão Geométrica do Raphael"); print ("\n")
print ("Para continuar, pressione 'Enter' \nPara sair, digite 's'"); print ("\n")
n = input ()
if n == "s":
    msg_adeus()

# Menu de opções:

while n != "s":
    if a == "s" or b == "s" or n == "s" or a == "3":
        break
    a = ""
    b = ""
    n = ""
    print ("\n"); menu()
    n = input ()
    while n != "1" and n != "2" and n != "3" and n != "4" and n != "5":
        print ("*alternativa inválida*"); menu(); n = input ()
    # Sair:

    if n == "5":
        msg_adeus()
        break

    # Termo Geral da Progressão (an):

    while n == "1":
        if a == "m" or a == "s" or b == "m" or b == "s" or n == "m" or n == "s" or a == "3" or a == "2":
            break
        # Entrada:

        informe()
        while True:
            try:        
                a = input ("1º termo da progressão (a1): ")
                if a == "s" or a == "m":
                    break
                else:
                    a = float(a)
                    break
            except ValueError or TypeError:
                print ("Entre com números!")
                if a == "s" or a == "m":
                    break
        if a == "s":
            msg_adeus()
            break
        elif a != "m":
            while True:
                try:
                    b = input ("Índice do termo desejado (n de an): ")
                    if b == "s" or b == "m":
                        break
                    else:
                        b = float(b)
                        break
                except ValueError or TypeError:
                    print ("Entre com números!")
                    if b == "s" or b == "m":
                        break
            if b == "s":
                msg_adeus()
                break
        if b != "m" and a != "m":
            while True:
                try:
                    n = input ("Razão da progressão (q): ")
                    if n == "s" or n == "m":
                        break
                    else:
                        n = float(n)
                        break
                except ValueError or TypeError:
                    print ("Entre com números!")
                    if n == "s" or n == "m":
                        break
            if n == "s":
                msg_adeus()
                break
        if n != "m" and a != "m" and b != "m":
            # Saída:

            print ("\n")
            print ("an =", a * n ** (b-1) )

            # Voltar ou Sair:

            voltar_sair()
            a = input ()
            if a == "3":
                msg_adeus()
                break
            elif a == "2":
                break
            elif a == "1":
                n = "1"

    # Razão da progressão (q):

    while n == "2":
        if a == "m" or a == "s" or b == "m" or b == "s" or n == "m" or n == "s" or a == "3" or a == "2":
            break
        # Entrada:
        informe()
        while True:
            try:        
                b = input ("Algum termo da progressão (an): ")
                if b == "s" or b == "m":
                    break
                else:
                    b = float(b)
                    break
            except ValueError or TypeError:
                print ("Entre com números!")
                if b == "s" or b == "m":
                    break
        if b == "s":
            msg_adeus()
            break
        if b != "m":
            while True:
                try:        
                    a = input ("Termo anterior (an - 1): ")
                    if a == "s" or a == "m":
                        break
                    else:
                        a = float(a)
                        break
                except ValueError or TypeError:
                    print ("Entre com números!")
                    if a == "s" or a == "m":
                        break
            if a == "s":
                msg_adeus()
                break
        if a != "m" and b != "m":
            # Saída:

            print ("\n")
            print ("q =", b / a)

            # Voltar ou Sair:

            voltar_sair()
            a = input ()
            if a == "3":
                msg_adeus()
                break
            elif a == "2":
                break
            elif a == "1":
                n = "2"
    
    # Soma geral FINITA dos termos da progressão (Sn):

    while n == "3":
        if a == "m" or a == "s" or b == "m" or b == "s" or n == "m" or n == "s" or a == "3" or a == "2":
            break
        # Entrada:

        informe()
        while True:
            try:        
                a = input ("1º termo da progressão (a1): ")
                if a == "s" or a == "m":
                    break
                else:
                    a = float(a)
                    break
            except ValueError or TypeError:
                print ("Entre com números!")
                if a == "s" or a == "m":
                    break
        if a == "s":
            msg_adeus()
            break
        if a != "m":
            while True:
                try:
                    b = input ("Razão da progressão (q): ")
                    if b == "s" or b == "m":
                        break
                    else:
                        b = float(b)
                        break
                except ValueError or TypeError:
                    print ("Entre com números!")
                    if b == "s" or b == "m":
                        break
            if b == "s":
                msg_adeus
                break
        if a != "m" and b != "m":
            while True:
                try:
                    n = input ("Quantidade de termos (n) da progressão: ")
                    if n == "s" or n == "m":
                        break
                    else:
                        n = float(n)
                        break
                except ValueError or TypeError:
                    print ("Entre com números!")
                    if n == "s" or n == "m":
                        break
            if n == "s":
                msg_adeus
                break
        if a != "m" and b != "m" and n != "m":
            # Saída:

            print ("\n")
            try:
                print ("Sn =", (a * (b ** n - 1)) / b - 1)
            except OverflowError:
                print ("Resultado grande demais, meu nobre :/")
            # Voltar ou Sair:

            voltar_sair()
            a = input ()
            if a == "3":
                msg_adeus()
                break
            elif a == "2":
                break
            elif a == "1":
                n = "3"

    # Soma geral INFINITA dos termos da progressão (s∞):

    while n == "4":
        if a == "m" or a == "s" or b == "m" or b == "s" or n == "m" or n == "s" or a == "3" or a == "2":
            break
        # Entrada:

        informe()
        while True:
            try:        
                a = input ("1º termo da progressão (a1): ")
                if a == "s" or a == "m":
                    break
                else:
                    a = float(a)
                    break
            except ValueError or TypeError:
                print ("Entre com números!")
                if a == "s" or a == "m":
                    break
        if a == "s":
            msg_adeus()
            break
        if a != "m":
            while True:
                try:
                    b = input ("Razão da progressão (q): ")
                    if b == "s" or b == "m":
                        break
                    else:
                        b = float(b)
                        break
                except ValueError or TypeError:
                    print ("Entre com números!")
                    if b == "s" or b == "m":
                        break
            if b == "s":
                msg_adeus()
                break
        if a != "m" and b != "m":

            # Saída:

            print ("\n")
            print ("s∞ =", a / 1 - b)

            # Voltar ou Sair:

            voltar_sair()
            a = input ()
            if a == "3":
                msg_adeus()
                break
            elif a == "2":
                break
            elif a == "1":
                n = "4"