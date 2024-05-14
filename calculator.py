""""
Variáveis:
a
b
r
op1
op2
op3
"""
print ("\n")
print ("Bem-vindo(a) à Calculadora do Raphael"); print ("\n")
op3 = "="
op1 = ""
while op1 != "a":
    # 1ª parte: a + b = r :
    a = input ("Número: ")
    while op1 != "a":
        # 3ª parte - loop:
        if op3 != "=":
            b = input("Número: ")
        else:
            op1 = input("Operação: ")
            b = input("Número: ")
        if op1 == "+":
            r = float(a) + float(b)
        elif op1 == "-":
            r = float(a) - float(b)
        elif op1 == "*":
            r = float(a) * float(b)
        elif op1 == "/":
            r = float(a) / float(b)
        elif op1 == "//":
            r = float(a) // float(b)
        elif op1 == "%":
            r = float(a) % float(b)
        elif op1 == "^" or op1 == "**":
            r = float(a) ** float(b)
        elif op1 == "=":
            print (r)
        op2 = input ("Operação: ")
        if op2 == "=":
            print ("\n")
            print (r)
            print ("\n")
            break
        
        # 2ª parte: r + b = a :
        b = input ("Número: ")
        if op2 == "+":
            a = float(r) + float(b)
        elif op2 == "-":
            a = float(r) - float(b)
        elif op2 == "*":
            a = float(r) * float(b)
        elif op2 == "/":
            a = float(r) / float(b)
        elif op2 == "//":
            a = float(r) // float(b)
        elif op2 == "%":
            a = float(r) % float(b)
        elif op2 == "^" or op3 == "**":
            a = float(r) ** float(b)
        op3 = input ("Operação: ")
        if op3 == "=":
            print ("\n")
            print (a)
            break