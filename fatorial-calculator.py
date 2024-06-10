""""
Variáveis:
a = fatorial de b
b = número que se deseja ser calculado o fatorial
c = variável contadora
"""

# Boas-vindas:

print ("\nBem-vindo(a) à Calculadora de Fatorial do Raphael\n")
a = ""

while a != "s":

    # Entrada:

    print ("*para sair, digite 's'* \nEntre com o número inteiro para fatorial:\n")
    while True:
        try: 
            a = input ()
            if a == "s":
                break
            a = int(a)
            break
        except ValueError or TypeError:
            print ("Entre com um número inteiro!")
    if a == "s":
        break

    # Cálculo:

    b = a
    c = a - 1
    for c in range (int(c), 1, -1):
        a = a * c

    # Saída:

    try:
        print ("\nO fatorial de", b, "é", a)
    except ValueError:
        print ("excedente ao limite (4300 dígitos) suportado :/")
    print ("")
print ("\nAdeus")