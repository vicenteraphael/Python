def msg_adeus():
    print ("\n"); print ("Adeus!")
print ("\n")
print ("Bem-vindo à Calculadora de Raízes de Equações Quadráticas do Raphael Vicente"); print ("\n")
print ("Pressione 'Enter' para continuar \nPara sair, digite 's'"); print ("\n")
a = input(); print ("\n"); print ("\n")
if a == "s":
    print ("Adeus!")
while a != "s":
    print ("Entre com os números dos coeficientes: \n*para sair, digite 's'*"); print ("\n")
    a = input ("a = ")
    if a == "s":
        msg_adeus()
        break
    while a.isalpha() == True:
        print ("Entre um número!")
        a = input ("a = ")
        if a == "s":
            print ("\n")
            print ("Adeus!")
            break
    b = input ("b = ")
    if b == "s":
        msg_adeus()
        break
    while b.isalpha() == True:
        print ("Entre um número!")
        b = input ("b = ")
        if b == "s":
            msg_adeus()
            break
    c = input ("c = ")
    if c == "s":
        msg_adeus()
        break
    while c.isalpha() == True:
        print ("Entre um número!")
        c = input ("c = ")
        if c == "s":
            msg_adeus()
            break
    if float(a) != 0:
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