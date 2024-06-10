"""
Variáveis e Funções:
a = 1º termo (a1)
b = 2º termo (an); razão (r); último termo (an)
n = escolha do menu; índice do termo desejado (n de an); índice do último termo (n de an)
"""
n = ''; a = ''; b = ''

# Boas-Vindas

print ("\nBem-vindo(a) à Calculadora de Progressão Aritmética do Raphael\n")

    # Menu de opções:

while n != "s" and a != "s" and b != "s":
    print ("\nVocê deseja calcular: \n\n1) Todos os termos da progressão \n2) Um termo n da progressão (an) \n3) A razão da progressão (r) \n4) A soma geral dos termos da progressão (Sn) \n5) Sair\n")
    n = input ()
    while n != "1" and n != "2" and n != "3" and n != "4" and n != "5" and n != "s":
        print ("\n*alternativa inválida*")
        print ("Você deseja calcular: \n\n1) Todos os termos da progressão \n2) Um termo n da progressão (an) \n3) A razão da progressão (r) \n4) A soma geral dos termos da progressão (Sn) \n5) Sair\n")
        n = input ()
    if n == "5" or n == "s":
        break

    # Todos os termos da progressão:

    if n == "1":
        print ("\n*Para sair, entre com 's'. Para voltar ao menu de opções, entre com 'm'* \nInforme-me:\n")
        while n == "1":
            while True:
                try:
                    a = input ("1º termo da progressão (a1): ")
                    if a == "s" or a == "m":
                        break
                    a = float(a)
                    break
                except ValueError or TypeError:
                    print ("Entre com um número!")                
            if a == "s" or a == "m":
                break
            while True:
                try:
                    b = input ("Último termo da progressão (an): ")
                    if b == "s" or b == "m":
                        break
                    b = float(b)
                    break
                except ValueError or TypeError:
                    print ("Entre com um número!")                
            if b == "s" or b == "m":
                break
            while True:
                try:
                    n = input ("Razão da progressão (r): ")
                    if n == "s" or n == "m":
                        break
                    n = float(n)
                    break
                except ValueError or TypeError:
                    print ("Entre com um número!")                
            if n == "s" or n == "m":
                break

            # Saída:

            print ("\nTodos os termos: ")
            while a <= b:
                if a == b:
                    print ("{}".format(a))
                elif a == b - n:
                    print ("{} e ".format(a), end='')
                else:
                    print ("{}, ".format(a), end='')
                a += n
            n = "1"; print ("")

    # Termo n da progressão (an):

    elif n == "2":
        print ("\n*Para sair, entre com 's'. Para voltar ao menu de opções, entre com 'm'* \nInforme-me:\n")
        while n == "2":
            while True:
                try:
                    a = input ("1º termo da progressão (a1): ")
                    if a == "s" or a == "m":
                        break
                    a = float(a)
                    break
                except ValueError or TypeError:
                    print ("Entre com um número!")                
            if a == "s" or a == "m":
                break
            while True:
                try:
                    b = input ("Razão da progressão (r): ")
                    if b == "s" or b == "m":
                        break
                    b = float(b)
                    break
                except ValueError or TypeError:
                    print ("Entre com um número!")                
            if b == "s" or b == "m":
                break
            while True:
                try:
                    n = input ("Índice do termo desejado (n de an): ")
                    if n == "s" or n == "m":
                        break
                    n = float(n)
                    break
                except ValueError or TypeError:
                    print ("Entre com um número!")                
            if n == "s" or n == "m":
                break

            # Saída:

            print ("\nan =", a + (n - 1) * b); n = "2"; print ("")

    # Razão da progressão:

    if n == "3":
        print ("\n*Para sair, entre com 's'. Para voltar ao menu de opções, entre com 'm'*\nInforme-me dois termos consecutivos da progressão:\n")
        while n == "3":
            while True:
                try:
                    a = input ("1º termo: ")
                    if a == "s" or a == "m":
                        break
                    a = float(a)
                    break
                except ValueError or TypeError:
                    print ("Entre com um número!")                
            if a == "s" or a == "m":
                break
            while True:
                try:
                    b = input ("2º termo: ")
                    if b == "s" or b == "m":
                        break
                    b = float(b)
                    break
                except ValueError or TypeError:
                    print ("Entre com um número!")                
            if b == "s" or b == "m":
                break

            # Saída:

            print ("\nr =", b - a); n = "3"; print ("")
    
    # Soma geral dos termos (Sn):

    if n == "4":
        print ("\n*Para sair, entre com 's'. Para voltar ao menu de opções, entre com 'm'* \nInforme-me:\n")
        while n == "4":
            while True:
                try:
                    a = input ("1º termo da progressão (a1): ")
                    if a == "s" or a == "m":
                        break
                    a = float(a)
                    break
                except ValueError or TypeError:
                    print ("Entre com um número!")                
            if a == "s" or a == "m":
                break
            while True:
                try:
                    b = input ("Último termo da progressão (an): ")
                    if b == "s" or b == "m":
                        break
                    b = float(b)
                    break
                except ValueError or TypeError:
                    print ("Entre com um número!")                
            if b == "s" or b == "m":
                break
            while True:
                try:
                    n = input ("Índice do último termo da progressão (n de an): ")
                    if n == "s" or n == "m":
                        break
                    n = float(n)
                    break
                except ValueError or TypeError:
                    print ("Entre com um número!")                
            if n == "s" or n == "m":
                break

            # Saída:

            print ("\nSn =", ((a + b) * n ) / 2); n = "4"; print ("")

print ("\nAdeus!")