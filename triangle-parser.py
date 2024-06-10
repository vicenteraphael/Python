"""
Variáveis e Funções:
a = lado do triângulo oposto ao ângulo Alfa
b = lado do triângulo oposto ao ângulo Beta
c = lado do triângulo oposto ao ângulo Theta
r = variável resposta 
sina = seno de Alfa
cosa = cosseno de Alfa
tga = tangente de Alfa
sinb = seno de Beta
cosb = cosseno de Beta
tgb = tangente de Beta
sinc = seno de Theta
cosc = cosseno de Theta
tgc = tangente de Theta
"""

# Boas-vindas:

print ("\nBem-vindo(a) à Calculadora Trigonométrica do Raphael\n")
a = ''
while a != "s":

    #Valores de Entrada:

    print ("Entre com os valores do Triângulo: \n*Para sair, digite 's'*\n")
    while True:
        try:
            a = input ("1º lado (a): ")
            if a == "s":
                break
            a = float(a)
            break
        except ValueError or TypeError:
            print ("Entre com um número!")
    if a == "s":
        break
    while True:
        try:
            b = input ("2º lado (b): ")
            if b == "s":
                break
            b = float(b)
            break
        except ValueError or TypeError:
            print ("Entre com um número!")
    if b == "s":
        break
    while True:
        try:
            c = input ("3º lado (c): ")
            if c == "s":
                break
            c = float(c)
            break
        except ValueError or TypeError:
            print ("Entre com um número!")
    if c == "s":
        break
    print ("")

    #Tipo de Triângulo e saída:

    if a < b + c and b < a + c and c < a + b:    
        if a == b and b == c:
            print ("O Triângulo é Equilátero")
        elif a == b or b == c or b == a:
            print ("O Triângulo é Isósceles")
        elif a != b and b != c and a != c:
            print ("O Triângulo é Escaleno")
        if a**2 == b**2 + c**2 or b**2 == a**2 + c**2 or c**2 == b**2 + a**2:
            print ("O triângulo é Retângulo")
        print ("\nDesejas: \n\n1) Calcular Seno, Cosseno e Tangente \n2) Voltar ao início \n3) Sair\n")
        r = input ()
        if r != "1" and r != "2" and r != "3":
            print ("\n*alternativa inválida*")
            print ("Desejas: \n\n1) Calcular Seno, Cosseno e Tangente \n2) Voltar ao início \n3) Sair\n")
            r = input ()
        elif r == "3":
            break
        elif r == "1":

        # Cálculo Trigonométrico:

            print ("\nTendo Alfa como sendo o ângulo oposto ao lado a:", a ,"\n Beta sendo o ângulo oposto ao lado b:", b,"\ne Theta sendo o ângulo oposto ao lado c:", c,"\n")
            cosa = (a**2 - (b**2 + c**2)) / (- 2 * b * c)
            sina = (1 - cosa**2) ** 0.5
            tga = sina / cosa
            cosb = (b**2 - (a**2 + c**2)) / (- 2 * a * c)
            sinb = (1 - cosb**2) ** 0.5
            tgb = sinb / cosb
            cosc = (c**2 - (a**2 + b**2)) / (- 2 * a * b)
            sinc = (1 - cosc**2) ** 0.5
            tgc = sinc / cosc

            # Saída:

            print ("seno de Alfa =", sina, "      cosseno de Alfa =", cosa, "      tangente de Alfa =", tga)
            print ("seno de Beta =", sinb, "      cosseno de Beta =", cosb, "      tangente de Beta =", tgb)
            print ("seno de Theta =", sinc, "      cosseno de Theta =", cosc, "      tangente de Theta =", tgc)
            print ("\nPara continuar, pressione 'Enter'. Para sair, digite 's'\n")
            r = input ()
            if r == "s":
                break
    else:
        print ("Os valores dados não formam um triângulo :/")
    print ("")

print ("\nAdeus!")