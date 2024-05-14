""""
Variáveis:
a = variável contadora
b = termo n da sequência
c = antecessor de b
n = antecessor sucessivo de b
"""

# Boas-vindas:

print ("\n")
print ("Bem-vindo(a) à Calculadora de Fibonacci do Raphael")
a = ""
while a != "s":

    #Índice da sequência:

    print ("\n")
    print ("Desejas que a sequência de fibonacci seja exibida até qual termo? \n*para sair, digite 's'*"); print ("\n")
    a = input ()
    if a == "s":
        print ("\n")
        print ("Adeus!")
        break
    while a.isnumeric() == False:
        print ("*Entre com um número inteiro*")
        print ("Desejas que a sequência de fibonacci seja exibida até qual termo? \n*para sair, digite 's'*"); print ("\n")
        a = input (); print ("\n")
        if a == "s":
            break
    if a == "s":
        print ("Adeus!")
        break

    # Cálculo e Saída:

    print ("Aqui está a sequência de Fibonacci exibida até o", a,"º", "termo:"); print ("\n")
    a = int(a)
    b = 0
    c = 1
    n = 0
    print ("1 º: 1")
    for a in range (2, a + 1):
        b = c + n
        n = c
        c = b
        print (a,"º:",  b)
