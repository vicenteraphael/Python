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
    print ("\n*Para sair, entre com 's'. Para voltar ao menu de opções, entre com 'm'* \n\nInforme:\n")

def menu():
    print ("Desejas calcular: \n\n1) Todos os termos da progressão \n2) Um termo n da progressão (an) \n3) A razão da progressão (q) \n4) A soma geral FINITA dos termos da progressão (Sn) \n5) A soma geral INFINITA dos termos da progressão (s∞) \n6) Sair \n")

# Boas vindas:

print ("\nBem-vindo(a) à Calculadora de Progressão Geométrica do Raphael\n")

# Menu de opções:

while n != "s" and a != "s" and b != "s":
    menu()
    n = input ()
    while n != "1" and n != "2" and n != "3" and n != "4" and n != "5" and n != "6" and n != "s":
        print ("*alternativa inválida*"); menu(); n = input ()
    if n == "6" or n == "s":        
        break
    
    # Todos os Termos da Progressão:

    if n == "1":
        informe()
        while n == "1":
            
            # Entrada:

            while True:
                try:        
                    a = input ("1º termo da progressão (a1): ")
                    if a == "s" or a == "m":
                        break
                    a = float(a)
                    break
                except ValueError or TypeError:
                    print ("Entre com números!")
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
                    print ("Entre com números!")
            if b == "s" or b == "m":                
                break
            while True:
                try:
                    n = input ("Razão da progressão (q): ")
                    if n == "s" or n == "m":
                        break
                    n = float(n)
                    break
                except ValueError or TypeError:
                    print ("Entre com números!")
            if n == "s" or n == "m":                
                break

            # Saída:

            print ("\nTodos os termos:\n")
            while a <= b:
                if a == b:
                    print (a)
                elif a == b / n:
                    print ("{} e " .format(a), end='')
                else:
                    print ("{}, " .format(a), end='')
                a *= n
            n = "1"; print ("")

    # Termo Geral da Progressão (an):

    elif n == "2":
        informe()
        while n == "2":
            
            # Entrada:

            while True:
                try:        
                    a = input ("1º termo da progressão (a1): ")
                    if a == "s" or a == "m":
                        break
                    a = float(a)
                    break
                except ValueError or TypeError:
                    print ("Entre com números!")
            if a == "s" or a == "m":            
                break
            while True:
                try:
                    b = input ("Índice do termo desejado (n de an): ")
                    if b == "s" or b == "m":
                        break
                    b = float(b)
                    break
                except ValueError or TypeError:
                    print ("Entre com números!")
            if b == "s" or b == "m":                
                break
            while True:
                try:
                    n = input ("Razão da progressão (q): ")
                    if n == "s" or n == "m":
                        break
                    n = float(n)
                    break
                except ValueError or TypeError:
                    print ("Entre com números!")
            if n == "s" or n == "m":                
                break

            # Saída:

            print ("\nan =", a * n ** (b-1)); n = "2"; print ("")

    # Razão da progressão (q):

    elif n == "3":
        informe()
            
            # Entrada:

        while n == "3":    
            while True:
                try:        
                    b = input ("Algum termo da progressão (an): ")
                    if b == "s" or b == "m":
                        break
                    b = float(b)
                    break
                except ValueError or TypeError:
                    print ("Entre com números!")
            if b == "s" or b == "m":            
                break
            while True:
                try:        
                    a = input ("Termo anterior (an - 1): ")
                    if a == "s" or a == "m":
                        break
                    a = float(a)
                    break
                except ValueError or TypeError:
                    print ("Entre com números!")
            if a == "s" or a == "m":                
                break

            # Saída:

            print ("\nq =", b / a); n = "3"; print ("")
    
    # Soma geral FINITA dos termos da progressão (Sn):

    elif n == "4":
        informe()
            
            # Entrada:
        while n == "4":
            while True:
                try:        
                    a = input ("1º termo da progressão (a1): ")
                    if a == "s" or a == "m":
                        break
                    a = float(a)
                    break
                except ValueError or TypeError:
                    print ("Entre com números!")
            if a == "s" or a == "m":            
                break
            while True:
                try:
                    b = input ("Razão da progressão (q): ")
                    if b == "s" or b == "m":
                        break
                    b = float(b)
                    break
                except ValueError or TypeError:
                    print ("Entre com números!")
            if b == "s" or b == "m":
                break
            while True:
                try:
                    n = input ("Quantidade de termos (n) da progressão: ")
                    if n == "s" or n == "m":
                        break
                    n = float(n)
                    break
                except ValueError or TypeError:
                    print ("Entre com números!")
            if n == "s" or n == "m":
                break

            # Saída:

            try:
                print ("\nSn =", (a * (b ** n - 1)) / b - 1)
            except OverflowError:
                print ("Resultado grande demais, meu nobre :/")
            n = "4"; print ("")

    # Soma geral INFINITA dos termos da progressão (s∞):

    elif n == "5":
        informe()
            
            # Entrada:

        while n == "5":
            while True:
                try:        
                    a = input ("1º termo da progressão (a1): ")
                    if a == "s" or a == "m":
                        break
                    a = float(a)
                    break
                except ValueError or TypeError:
                    print ("Entre com números!")
            if a == "s" or a == "m":            
                break
            while True:
                try:
                    b = input ("Razão da progressão (q): ")
                    if b == "s" or b == "m":
                        break
                    b = float(b)
                    break
                except ValueError or TypeError:
                    print ("Entre com números!")
            if b == "s" or b == "m":                
                break            

            # Saída:

            print ("\ns∞ =", a / 1 - b); n = "5"; print ("")

print ("\nAdeus!")