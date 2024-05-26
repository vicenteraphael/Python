print ("\nBem-vindo(a) ao Programa de Calculadora de Divisores do Raphael\n")
a = ""
while a != "s" and a != "4":
    print ("Desejas calcular: \n\n1) Divisores de uma sequência \n2) Primos de uma sequência \n3) Máximo Divisor Comum (MDC) \n4) Mínimo Múltiplo Comum (MMC) \n5) Sair\n")
    a = input()
    while a != "1" and a != "2" and a != "3" and a != "4" and a != "5":
        print ("Alternativa inválida!")
        print ("Desejas calcular: \n\n1) Divisores de uma sequência \n2) Máximo Divisor Comum (MDC) \n3) Mínimo Múltiplo Comum (MMC) \n4) Sair\n")        
        a = input()
    if a == "5":
        break
    while a == "1":
        n = []
        print ("\n*para sair, entre com 's'. Para voltar ao menu inicial, entre com 'm'*\nInforme-me:\n\n")
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
        for _ in range (a, b + 1, c):
            n.append(_)
        n.sort()
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
        if len(c) == 0:
            print ("A quantidade de números divisíveis por", b, "de", n[0], "até", n[-1], "é", len(c), ".", "\n")
        else:
            print ("A quantidade de números divisíveis por", b, "de", n[0], "até", n[-1], "é", len(c), ". \nA saber:", c, "\n")
    
    while a == "2":
        n = []
        print ("\n*para sair, entre com 's'. Para voltar ao menu inicial, entre com 'm'*\nInforme-me:\n\n")
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
        for _ in range (a, b + 1, c):
            n.append(_)
        n.sort()
        while 1 in n:
            n.remove(1)
        while 0 in n:
            n.remove(0)
        dt = []
        for a in n:
            c = 2
            while c < a:
                if a % c == 0:
                    dt.append(a)
                    break
                c += 1
        for a in dt:
            n.remove(a)
        print (n)

    while a == "3":
        print ("\n*para sair, entre com 's'. Para voltar ao menu inicial, entre com 'm'*\nInforme-me os números inteiros os quais você deseja saber o MDC \nQuando finalizar, entre com '='\n")
        b = []
        while a != "=":
            try:
                a = input()
                if a == "s" or a == "m" or a == "=":
                    break
                b.append(int(a))
            except:
                print ("Entre com um número inteiro!")
        b.sort()
        c = 2
        a = []
        for _ in b:
            if len(a) > 0:
                c = max(a)
                if _ % c != 0:
                    c = 0
                    break
            elif len(a) == 0:
                while c < _:
                    if _ % c == 0:
                        a.append(c)
                    c += 1
        if c != 0:
            print (c)
        else:
            print ("Os números são primos entre si")