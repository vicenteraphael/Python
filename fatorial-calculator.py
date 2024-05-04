""""
Variáveis:
num = fatorial de fat
fat = número que se deseja ser calculado o fatorial
cont = variável contadora
"""

# Boas-vindas:

print ("\n")
print ("Bem-vindo à Calculadora de Fatorial do Raphael Vicente"); print ("\n")
num = ""

while num != "s":

    # Entrada:

    print ("*para sair, digite 's'* \nEntre com o número inteiro para fatorial:"); print ("\n")
    while True:
        try: 
            num = input ()
            if num == "s":
                break
            else:
                num = int(num)
            break
        except ValueError or TypeError:
            print ("\n")
            print ("Entre com um número inteiro! \n*para sair, digite 's'*"); print ("\n")
            if num == "s":
                break
    if num == "s":
        print ("\n")
        print ("Adeus!")
        break

    # Cálculo:

    fat = num
    cont = num - 1
    for cont in range (int(cont), 1, -1):
        num = num * cont
    print ("\n")

    # Saída:

    try:
        print ("O fatorial de", fat, "é", num); print ("\n")
    except ValueError:
         print ("excedente ao limite (4300 dígitos) suportado :/")
    print ("\n")