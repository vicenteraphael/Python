""""
Variáveis:
a = fatorial de b
b = número que se deseja ser calculado o fatorial
c = variável contadora
"""

# Boas-vindas:

print ("\n")
print ("Bem-vindo(a) à Calculadora de fatorial do Raphael"); print ("\n")
a = ""

while a != "s":

    # Entrada:

    print ("*para sair, digite 's'* \nEntre com o número inteiro para fatorial:"); print ("\n")
    while True:
        try: 
            a = input ()
            if a == "s":
                break
            else:
                a = int(a)
            break
        except ValueError or TypeError:
            print ("\n")
            print ("Entre com um número inteiro! \n*para sair, digite 's'*"); print ("\n")
            if a == "s":
                break
    if a == "s":
        print ("\n")
        print ("Adeus!")
        break

    # Cálculo:

    b = a
    c = a - 1
    for c in range (int(c), 1, -1):
        a = a * c
    print ("\n")

    # Saída:

    try:
        print ("O fatorial de", b, "é", a); print ("\n")
    except ValueError:
         print ("excedente ao limite (4300 dígitos) suportado :/")
    print ("\n")