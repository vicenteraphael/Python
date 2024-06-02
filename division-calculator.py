print ("\nBem-vindo(a) ao Programa de Calculadora de Divisores do Raphael\n")
a = ""

# Menu inicial:

while a != "s" and a != "4":
    print ("Desejas calcular: \n\n1) Divisores de uma sequência \n2) Primos de uma sequência \n3) Máximo Divisor Comum (MDC) \n4) Mínimo Múltiplo Comum (MMC) \n5) Sair\n")
    a = input()
    while a != "1" and a != "2" and a != "3" and a != "4" and a != "5":
        print ("Alternativa inválida!")
        print ("Desejas calcular: \n\n1) Divisores de uma sequência \n2) Máximo Divisor Comum (MDC) \n3) Mínimo Múltiplo Comum (MMC) \n4) Sair\n")        
        a = input()
    if a == "5":
        break

    # Divisores de uma sequência:

    while a == "1":
        n = []
        print ("\n*para sair, entre com 's'. Para voltar ao menu inicial, entre com 'm'*\nInforme-me:\n\n")

        # Entrada dos termos da sequência:

        while True:
            try:
                a = input ("1º termo da sequência (a1): ")
                if a == "s" or a == "m":
                    break
                a = int(a)
                break
            except:
                print ("Entre com um número inteiro!")
        if a == "s" or a == "m":
            break
        while True:
            try:
                b = input ("Último termo da sequência (an): ")
                if b == "s" or b == "m":
                    break
                b = int(b)
                break
            except:
                print ("Entre com um número inteiro!")
        if b == "s" or b == "m":
            break
        while True:
            try:
                c = input ("Razão da sequência (r): ")
                if c == "s" or c == "m":
                    break
                c = int(c)
                break
            except:
                print ("Entre com um número inteiro!")
        if c == "s" or c == "m":
            break

        # Cálculo da Sequência:

        for _ in range (a, b + 1, c):
            n.append(_)
        n.sort()

        # Entrada dos divisores da sequência:

        print ("\nDesejas verificar se os termos da sua sequência são divisíveis por quais números?\nEntre com '=' quando terminar para ver o resultado\n")
        b = []
        while a != "=":
            try:
                a = input()
                if a == "s" or a == "m" or a == "=":
                    break
                b.append(int(a))
            except:
                print ("Entre com um número inteiro!")
        if a == "s" or a == "m":
            break

        # Cálculo:

        c = []
        a = 1
        for _ in b:
            a *= _
        for _ in n:
            if _ % a == 0:
                c.append(_)
        c.sort()
        a = -1
        dt = -10
        for _ in c:
            a += 1
            if _ == dt:
                c.remove(_)
            dt = _

        # Sáida:
        
        if len(c) == 0:
            print ("\nA quantidade de números divisíveis por ", end='')
            for _ in b:
                if len(b) == 1:
                    print (_, "", end='')
                else:
                    if _ == b[-2]:
                        print (_, "e " ,end='')
                    elif _ == b[-1]:
                        print (_,"",end='')
                    else:
                        print (_,", ",end='')
            print ("de", n[0], "até", n[-1], "é", len(c), "\n")
        else:
            print ("\nA quantidade de números divisíveis por ", end='')
            for _ in b:
                if len(b) == 1:
                    print (_, "", end='')
                else:
                    if _ == b[-2]:
                        print (_, "e " ,end='')
                    elif _ == b[-1]:
                        print ("{}; ".format(_), end='')
                    else:
                        print ("{}, ".format(_), end='')
            print ("de", n[0], "até {};".format(n[-1]), "razão {},".format(n[2] - n[1]) ,"é", len(c), "\nA saber: ", end='')
            for _ in c:
                if len(c) == 1:
                    print (_, "\n")
                else:
                    if _ == c[-2]:
                        print (_, "e ", end='')
                    elif _ == c[-1]:
                        print (_, "\n")
                    else:
                        print ("{}, ".format(_), end='')
    
    # Primos de uma sequência:

    while a == "2":

        n = []
        print ("\n*para sair, entre com 's'. Para voltar ao menu inicial, entre com 'm'*\nInforme-me:\n\n")
        
        # Entrada:
        
        while True:
            try:
                a = input ("1º termo da sequência (a1): ")
                if a == "s" or a == "m":
                    break
                a = int(a)
                break
            except:
                print ("Entre com um número inteiro!")
        if a == "s" or a == "m":
            break
        while True:
            try:
                b = input ("Último termo da sequência (an): ")
                if b == "s" or b == "m":
                    break
                b = int(b)
                break
            except:
                print ("Entre com um número inteiro!")
        if b == "s" or b == "m":
            break
        while True:
            try:
                c = input ("Razão da sequência (r): ")
                if c == "s" or c == "m":
                    break
                c = int(c)
                break
            except:
                print ("Entre com um número inteiro!")
        if c == "s" or c == "m":
            break

        # Cálculo:

        for _ in range (a, b + 1, c):
            n.append(_)
        n.sort()
        while 1 in n:
            n.remove(1)
        while 0 in n:
            n.remove(0)
        dt = []
        for _ in n:
            x1 = 2
            while x1 < _:
                if _ % x1 == 0:
                    dt.append(_)
                    break
                x1 += 1
        for _ in dt:
            n.remove(_)

        # Saída:

        if len(n) == 0:
            print ("\nA quantidade de números primos de", a, "até {},".format(b), "razão {}, é 0".format(c))
        else:
            print ("\nA quantidade de números primos de", a, "até {},".format(b), "razão {}," .format(c), "é", len(n), "\nA saber: ", end='')
        for _ in n:
            if len(n) == 1:
                print (_)
            else:
                if _ == n[-2]:
                    print (_,"e ", end='')
                elif _ == n[-1]:
                    print (_)
                else:
                    print ('{}, '.format(_), end='')

    # Máximo Divisor Comum (MDC):

    while a == "3":
        print ("\n*para sair, entre com 's'. Para voltar ao menu inicial, entre com 'm'*\nInforme-me os números inteiros os quais você deseja saber o MDC \nQuando finalizar, entre com '='\n")
        b = []

        # Entrada:

        while a != "=":
            try:
                a = input()
                if a == "s" or a == "m" or a == "=":
                    break
                b.append(int(a))
            except:
                print ("Entre com um número inteiro!")
            if a == "s":
                break
        if a != "m":
            b.sort()

            # Cálculo:

            if 0 in b:
                b.append(0)
                b.remove(0)
            c = 0
            dt = b[0]
            a = []
            for _ in b:
                if _ == 0:
                    c += 1
                    break
                if _ % dt == 0:
                    c += 1
                else:
                    c = 0
                    break
            dt = 0
            if c != len(b):
                c = 2
                if len(a) == 0:
                    while c < b[0]:
                        if b[0] % c == 0:
                            a.append(c)
                        c += 1
                    a.sort()
                    a.reverse()
                c = 0
                x1 = 0
                for dt in a:
                    for _ in b:
                        if _ != b[0]:
                            if _ % dt == 0:
                                x1 += 1
                            if x1 == (len(b) - 1):
                                c = dt
                                break
                            if _ % dt != 0:
                                x1 = 0
                                break
                    if x1 == (len(b) - 1):
                        break

                # Saída MDC != menor número:

                if c != 0:
                    print ("\nO MDC de ",end='')
                    for _ in b:
                        if _ == b[-2]:
                            print (_, "e ", end='')
                        elif _ == b[-1]:
                            print (_, end='')
                        else:
                            print ("{}, ".format(_), end='')
                    print (" é {}".format(c))
                else:
                    print ("\nOs números ", end='')
                    for _ in b:
                        if _ == b[-2]:
                            print ("{} e ".format(_), end='')
                        elif _ == b[-1]:
                            print (_, end='')
                        else:
                            print ("{}, ".format(_), end='')
                    print (" são primos entre si")
            
            # Saída MDC = menor número:

            else:
                print ("\nO MDC de ",end='')
                for _ in b:
                    if _ == b[-2]:
                        print (_, "e ", end='')
                    elif _ == b[-1]:
                        print (_, end='')
                    else:
                        print ("{}, ".format(_), end='')
                print (" é {}".format(b[0]))
    
    # Mínimo Múltiplo Comum (MMC):

    while a == "4":
        print ("\n*para sair, entre com 's'. Para voltar ao menu inicial, entre com 'm'*\nInforme-me os números inteiros os quais você deseja saber o MDC \nQuando finalizar, entre com '='\n")
        b = []

        # Entrada:

        while a != "=":
            try:
                a = input()
                if a == "s" or a == "m" or a == "=":
                    break
                b.append(int(a))
            except:
                print ("Entre com um número inteiro!")
            if a == "s":
                break

        # Cálculo:

        b.sort()
        c = 0
        _ = 0
        while True:
            _ += 1
            for a in b:
                if (_ * b[-1]) % a == 0:
                    c += 1
                else:
                    c = 0
                    break
            if c == len(b):
                break

        # Sáida:

        print ("O MMC de ", end='')
        for a in b:
            if a == b[-1]:
                print (a, end='')
            elif a == b[-2]:
                print ("{} e ".format(a), end='')
            else:
                print ("{}, ".format(a), end='')
        print (" é", int(_ * b[-1]))
        
print ("\nAdeus!")