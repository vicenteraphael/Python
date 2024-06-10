"""
Variáveis e Funções:
a = coeficiente a 
b = coeficiente b
c = coeficiente c
dt = delta
x1 = x'
x2 = x''
"""

# Boas-vindas:

print ("\nBem-vindo(a) à Calculadora de Raízes de Equações Quadráticas do Raphael\n")
print ("Pressione 'Enter' para continuar \nPara sair, digite 's'")
a = input()

# Entrada dos Coeficientes:   

while a != "s":
    print ("Entre com os números dos coeficientes: \n*para sair, entre com 's'*"); print ("\n")
    while True:
        try:
            a = input ("a = ")
            if a == "s":
                break
            a = float(a)
            break
        except ValueError or TypeError:
            print ("Entre com um número!")
            if a == "s":
                break
    if a == "s":
        break
    while True:
        try:
            b = input ("b = ")
            if b == "s":
                break
            b = float(b)
            break
        except ValueError or TypeError:
            print ("Entre com um número!")
            if b == "s":
                break
    if b == "s":
        break
    while True:
        try:
            c = input ("c = ")
            if c == "s":
                break
            c = float(c)
            break
        except:
            print ("Entre com um número!")
            if c == "s":
                break
    if c == "s":
        break

    # Cálculo das Raízes:

    if a != 0:
        dt = b ** 2 - 4 * a * c
        x1 = (- b + dt ** 0.5) / (2 * a)
        x2 = (- b - dt ** 0.5) / (2 * a)

        # Saída e/ou Ponderações:

        if dt == 0:
            print ("\nAs raízes são iguais:", x1)
        elif dt < 0:
            print ("\nA equaçaõ não possui solução real")
        else:
            print ("\nx' = ", x1, "\nx'' = ", x2)
    else:
        print ("\nOs coeficientes não formam uma equação quadrática!")
print ("\nAdeus!")