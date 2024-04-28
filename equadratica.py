print ("\n")
print ("Bem-vindo à Calculadora de Raízes de Equações Quadráticas do Raphael Vicente"); print ("\n")
a = ""
while a != 0:
    print ("*para sair, digite 's'* \nEntre com os números dos coeficientes:"); print ("\n")
    a = input ("a = ")
    if a == "s":
        print ("Adeus!")
        break
    while a.isdigit() == False:
        print ("Entre um número!")
        a = input ("a = ")
        if a == "s":
            print ("Adeus!")
            break
        break
    b = input ("b = ")
    if b == "s":
        print ("Adeus!")
        break
    while b.isdigit() == False:
        print ("Entre um número!")
        b = input ("b = ")
        if b == "s":
            print ("Adeus!")
            break
    c = input ("c = ")
    if c == "s":
        print ("Adeus!")
        break
    while c.isdigit() == False:
        print ("Entre um número!")
        c = input ("c = ")
        if c == "s":
            print ("Adeus!")
            break
    if int(a) != 0:
        dt = float(b) ** 2 - 4 * float(a) * float(c)
        x1 = (- float(b) + dt ** 0.5) / (2 * float(a))
        x2 = (- float(b) - dt ** 0.5) / (2 * float(a))
        if dt == 0:
            print ("\n")
            print ("As raízes são iguais:", x1); print ("\n")
        elif dt < 0:
            print ("\n")
            print ("A equaçaõ não possui solução real"); print ("\n")
        else:
            print ("\n")
            print ("x1 = ", x1, "\nx2 = ", x2); print ("\n")
    else:
        print ("Os coeficientes não formam uma equação quadrática!"); print ("\n")