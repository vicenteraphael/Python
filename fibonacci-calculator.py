""""
Variáveis:
cont = variável contadora
num = termo n da sequência
ant = antecessor de num
antsuc = antecessor sucessivo de num
"""

# Boas-vindas:

print ("\n")
print ("Bem-vindo à Calculadora de Fibonacci do Raphael"); print ("\n")
print ("Para iniciar, pressione 'Enter' \nPara sair, digite 's'"); print ("\n")
cont = input ()
if cont == "s":
    print ("\n")
    print ("Adeus!")
while cont != "s":

    #Índice da sequência:

    print ("\n")
    print ("Desejas ver a sequência de fibonacci exibida até qual termo? \n*para sair, digite 's'*"); print ("\n")
    cont = input (); print ("\n")
    if cont == "s":
        print ("Adeus!")
        break
    while cont.isnumeric() == False:
        print ("*Entre com um número inteiro*"); print ("\n")
        cont = input (); print ("\n")

    # Cálculo e Saída:

    print ("Aqui está a sequência de Fibonacci exibida até o", cont,"º", "termo:"); print ("\n")
    cont = int(cont)
    num = 0
    ant = 1
    antsuc = 0
    print ("1 º: 1")
    for cont in range (2, cont + 1):
        num = ant + antsuc
        antsuc = ant
        ant = num
        print (cont,"º:",  num)
