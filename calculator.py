print ("\n")
print ("Bem-vindo à Calculadora de Dois Dígitos do Raphael Vicente"), print ("\n")
a = ""
while a != "s":
    print ("*para sair, digite 's'* "); print ("\n")
    a = input ("Primeiro número: ")
    if a == "s":
        print ("\n")
        print ("Adeus!")
        break
    while a.isnumeric() == False:
        print ("\n")
        print ("*entre com números*")
        a = input ("Primeiro número: ")
        if a == "s":
            print ("\n")
            print ("Adeus!")
            break
    op = input ("Operação: ")
    if op == "s":
        print ("\n")
        print ("Adeus!")
        break
    while op != "+" and op != "-" and op != "*" and op != "/" and op != "//" and op != "%" and op != "**" and op != "^":
        print ("\n")
        print ("*operação inválida*")
        op = input ("Operação: ")
        if op == "s":
            print ("\n")
            print ("Adeus!")
            break
    b = input ("Segundo número: "); print ("\n")
    if b == "s":
        print ("\n")
        print ("Adeus!")
        break
    while b.isnumeric() == False:
        print ("\n")
        print ("*entre com números*")
        b = input ("Segundo número: ")
        if b == "s":
            print ("\n")
            print ("Adeus!")
            break
    if op == "+":
        r = float(a) + float(b)
        print (a, "+", b, "=", r)
    elif op == "-":
        r = float(a) - float(b)
        print (a, "-", b, "=", r)
    elif op == "*":
        r = float(a) * float(b)
        print (a, "*", b, "=", r)
    elif op == "/":
        r = float(a) / float(b)
        print (a, "/", b, "=", r)
    elif op == "//":
        r = float(a) // float(b)
        print (a, "//", b, "=", r)
    elif op == "%":
        r = float(a) % float(b)
        print (a, "%", b, "=", r)
    elif op == "^" or op == "**":
        r = float(a) ** float(b)
        print (a, "^", b, "=", r)
    else:
        print ("vocçê burlou o sistema!")