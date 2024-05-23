'''
Variáveis:
a
b
c
n
_
dt
'''
print ("\nBem-vindo ao Programa de Médias do Raphael\n")
a = ""
while a != "s" and a != "5":

    # Menu de opções:

    print ("Desejas calcular: \n\n1) Média Aritmética \n2) Média Ponderada \n3) Moda \n4) Mediana \n5) Sair\n")
    a = input ()
    while a != "1" and a != "2" and a != "3" and a != "4" and a != "5":
        print ("Escolha inválida!")
        a = input ()

    # Média Aritmética:

    while a == "1":
        print ("\nQuando quiser saber a média dos valores informados, entre com '=' \npara sair, entre com 's'\npara voltar ao menu de opções, entre com 'm'\n")
        while a != "s":
            b = []

            # Entrada:

            while True:
                try:
                    a = input ("Valor: ")
                    if a == "s" or a == "m" or a == "=":
                        break
                    a = float(a)
                    b.append(a)
                except:
                    print ("Entre com um número")
            if a == "s" or a == "m":
                break

            # Saída:

            print ("\nMÉDIA =",float(sum(b) / len(b)), "\n")

    # Média Ponderada:

    while a == "2":
        print ("\nQuando quiser saber a média dos valores informados, entre com '=' no lugar do valor \npara sair, entre com 's'\npara voltar ao menu de opções, entre com 'm'")
        while a != "=":
            b = []
            c = []
            n = []

            # Entrada:

            while True:
                try:
                    a = input("\nValor: ")
                    if a == "s" or a == "m" or a == "=":
                        break
                    a = float(a)
                    b.append(a)
                    a = input("Peso: ")
                    while a == "=":
                        print ("Todo valor deve ter um peso!")
                        a = input()
                    if a == "s" or a == "m" or a == "=":
                        break
                    a = float(a)
                    c.append(a)
                except:
                    print ("Entre com um número!")
            if a == "s" or a == "m":
                break

            # Cálculo / Saída:

            a = -1
            for _ in b:
                a += 1
                n.append(float(_ * c[a]))
            print ("\nMÉDIA =",sum(n) / sum(c),"\n")

    # Moda:

    while a == "3":
        print ("\nQuando quiser saber a moda dos valores informados, entre com '=' \npara sair, entre com 's'\npara voltar ao menu de opções, entre com 'm'\n")
        while a != "=":
            a = []

            # Entrada:

            while True:
                try:
                    b = input ()
                    if b == "s" or b == "m" or b == "=":
                        break
                    b = float(b)
                    a.append(b)
                except:
                    print ("Entre com um número!")
            if b == "s" or b == "m":
                a = ""
                a = b
                break
            b = []

            # Cálculo:

                # Moda de um único valor:
            if len(a) == 1:
                print ("\nMODA =",a[0], "\n")
            
            else:
                while len(a) != 0:
                    b.append(max(a))
                    a.remove(max(a))
                n = {}
                a = 0
                dt = b[1]
                for _ in b:
                    a += 1
                    if _ == dt:
                        n.update({_: a})
                    else:
                        a = 1
                    dt = _
                
            # Saída:

                if len(n) == 0:
                    print ("\nMODA =", b, "\n")
                else:
                    b = []
                    for a in n:
                        if n[a] == max(n.values()):
                            b.append(a)
                    print ("\nMODA =", b , "\n")

    # Mediana:

    while a == "4":
        print ("\nQuando quiser saber a mediana dos valores informados, entre com '=' \npara sair, entre com 's'\npara voltar ao menu de opções, entre com 'm'\n")
        while a != "=":
            b = []

            # Entrada:

            while True:
                try:
                    a = input ()
                    if a == "s" or a == "m" or a == "=":
                        break
                    a = float(a)
                    b.append(a)
                except:
                    print ("Entre com um número!")
            if a == "s" or a == "m":
                break

            # Cálculo:

            n = []
            while len(b) != 0:
                n.append(max(b))
                b.remove(max(b))
            dt = len(n) // 2

            # Saída:

            if len(n) % 2 != 0:
                print ("\nMEDIANA =", n[dt - 1], "\n")
            else:
                print ("\nMEDIANA =", (n[dt - 1] + n[dt]) / 2, "\n")
            a = str(a)