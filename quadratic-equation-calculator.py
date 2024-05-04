"""
Variáveis e Funções:
a = coeficiente a 
b = coeficiente b
c = coeficiente c
dt = delta
x1 = x'
x2 = x''
def msg_adeus()
"""

def msg_adeus():
    print ("\n"); print ("Adeus!")

# Boas-vindas:

print ("\n")
print ("Bem-vindo à Calculadora de Raízes de Equações Quadráticas do Raphael Vicente"); print ("\n")
print ("Pressione 'Enter' para continuar \nPara sair, digite 's'"); print ("\n")
a = input(); print ("\n"); print ("\n")
if a == "s":
    print ("Adeus!")

# Entrada dos Coeficientes:   

while a != "s":
    print ("Entre com os números dos coeficientes: \n*para sair, digite 's'*"); print ("\n")
    while True:
        try:
            a = input ("a = ")
            if a == "s":
                break
            else:
                a = float(a)
                break
        except ValueError or TypeError:
            print ("*para sair, digite 's'* \nEntre com um número!")
            if a == "s":
                break
    if a == "s":
        msg_adeus()
        break
    while True:
        try:
            b = input ("b = ")
            if b == "s":
                break
            else:
                b = float(b)
                break
        except ValueError or TypeError:
            print ("*para sair, digite 's'* \nEntre com um número!")
            if b == "s":
                break
    if b == "s":
        msg_adeus()
        break
    while True:
        try:
            c = input ("c = ")
            if c == "s":
                break
            else:
                c = float(c)
                break
        except:
            print ("*para sair, digite 's'* \nEntre com um número!")
            if c == "s":
                break
    if c == "s":
        msg_adeus()
        break

    # Cálculo das Raízes:

    if a != 0:
        dt = b ** 2 - 4 * a * c
        x1 = (- b + dt ** 0.5) / (2 * a)
        x2 = (- b - dt ** 0.5) / (2 * a)

        # Saída e/ou Ponderações:

        if dt == 0:
            print ("\n")
            print ("As raízes são iguais:", x1); print ("\n")
        elif dt < 0:
            print ("\n")
            print ("A equaçaõ não possui solução real"); print ("\n")
        else:
            print ("\n")
            print ("x' = ", x1, "\nx'' = ", x2); print ("\n")
    else:
        print ("Os coeficientes não formam uma equação quadrática!"); print ("\n")