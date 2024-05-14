"""
Variáveis e Funções:
a = 1º termo (a1)
b = 2º termo (an); razão (r); último termo (an)
n = escolha do menu; índice do termo desejado (n de an); índice do último termo (n de an)
num_invalido()
msg_adeus()
"""

def num_invalido():
    print ("\n")
    print ("*número inválido*")
def msg_adeus():
    print ("\n")
    print ("Adeus!")

# Boas-Vindas

print ("\n")
print ("Bem-vindo(a) à Calculadora de Progressão Aritmética do Raphael"); print ("\n")
print ("Para inciar, pressione 'Enter' \nPara sair, digite 's'"); print ("\n")
n = input ()
if n == "s":
    msg_adeus()

    # Menu de opções:

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

    # Razão da progressão:

    elif n == "2":
        print ("\n")
        print ("Informe-me dois termos consecutivos da progressão: \n*para sair, digite 's'*"); print ("\n")
        while True:
            try:
                a = input ("1º termo: ")
                if a == "s":
                    break
                else:
                    a = float(a)
                    break
            except ValueError or TypeError:
                print ("*entre com números!* \n*para sair, digite 's'*")
                if a == "s":
                    break
        if a == "s":
            msg_adeus()
            break
        while True:
            try:
                b = input ("2º termo: ")
                if b == "s":
                    break
                else:
                    b = float(b)
                    break
            except ValueError or TypeError:
                print ("*entre com números!* \n*para sair, digite 's'*")
                if b == "s":
                    break
        if b == "s":
            msg_adeus()
            break

        # Saída:

        print ("\n")
        print ("r =", b - a)

    # Termo n da progressão (an):

    elif n == "1":
        print ("\n")
        print ("*para sair, digite 's'* \nInforme-me:"); print ("\n")
        while True:
            try:
                a = input ("1º termo da progressão (a1): ")
                if a == "s":
                    break
                else:
                    a = float(a)
                    break
            except ValueError or TypeError:
                print ("*entre com números!* \n*para sair, digite 's'*")
                if a == "s":
                    break
        if a == "s":
            msg_adeus()
            break
        while True:
            try:
                b = input ("razão da progressão (r): ")
                if b == "s":
                    break
                else:
                    b = float(b)
                    break
            except ValueError or TypeError:
                print ("*entre com números!* \n*para sair, digite 's'*")
                if b == "s":
                    break
        if b == "s":
            msg_adeus()
            break
        while True:
            try:
                n = input ("índice do termo desejado (n de an): ")
                if n == "s":
                    break
                else:
                    n = float(n)
            except ValueError or TypeError:
                print ("*entre com números!* \n*para sair, digite 's'*")
                if n == "s":
                    break
        if n == "s":
            msg_adeus()
            break

        # Saída:

        print ("\n")
        print ("an =", a + (n - 1) * b)
    
    # Soma geral dos termos (Sn):

    elif n == "3":

        print ("\n")
        print ("*para sair, digite 's'* \nInforme-me:"); print ("\n")
        while True:
            try:
                a = input ("1º termo da progressão (a1): ")
                if a == "s":
                    break
                else:
                    a = float(a)
                    break
            except ValueError or TypeError:
                print ("*entre com números!* \n*para sair, digite 's'*")
                if a == "s":
                    break
        if a == "s":
            msg_adeus()
            break
        while True:
            try:
                b = input ("Último termo da progressão (an): ")
                if b == "s":
                    break
                else:
                    b = float(n)
                    break
            except ValueError or TypeError:
                print ("*entre com números!* \n*para sair, digite 's'*")
                if b == "s":
                    break
        if b == "s":
            msg_adeus()
            break
        while True:
            try:
                n = input ("Índice do último termo da progressão (n de an): ")
                if n == "s":
                    break
                else:
                    n = float(n)
                    break
            except ValueError or TypeError:
                print ("*entre com números!* \n*para sair, digite 's'*")
                if n == "s":
                    break
        if n == "s":
            msg_adeus()
            break

        # Saída:

        print ("\n")
        print ("Sn =", ((a + b) * n ) / 2)

    # Sair ou voltar ao Menu de opções:

    print ("\n")
    print ("Para voltar, pressione 'Enter' \nPara sair, entre com o número 4 ou com a letra 's'"); print ("\n")
    n = input ()
    if n == "4":
        msg_adeus()
        break
