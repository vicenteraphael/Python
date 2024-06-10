""""
Variáveis:
a = variável contadora
b = termo n da sequência
c = antecessor de b
n = antecessor sucessivo de b
"""

# Boas-vindas:

print ("\nBem-vindo(a) à Calculadora de Fibonacci do Raphael\n")
a = ""
while a != "s":

    #Índice da sequência:

    while True:
        try:
            print ("Desejas que a sequência de fibonacci seja exibida até qual termo? \n*para sair, digite 's'*\n")
            a = input()
            if a == "s" or a == "S":    
                break
            a = int(a)
            break
        except:
            print ("*Entre com um número inteiro*")
    if a == "s":
        break

    # Cálculo e Saída:

    print ("Aqui está a sequência de Fibonacci exibida até o", a,"º", "termo:\n")
    b = 0
    c = 1
    n = 0
    print ("1º: 1")
    for a in range (2, a + 1):
        b = c + n
        n = c
        c = b
        print ("{}º:".format(a), b)
    print ("")

print ("\nAdeus")
