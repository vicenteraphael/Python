print ("\n")
print ("Bem-vindo à Calculadora de Fatorial do Raphael Vicente"); print ("\n")
num = ""
while num != "s":
    print ("*para sair, digite 's'* \nEntre com o número inteiro para fatorial:"); print ("\n")
    num = input ()
    while num.isnumeric() == False:
        print ("\n")
        print ("Entre com um número inteiro! \n*para sair, digite 's'*"); print ("\n")
        num = input ()
        if num == "s":
            break
    if num == "s":
        print ("\n")
        print ("Adeus!")
        break
    fat = num
    cont = int(num) - 1
    for cont in range (int(cont), 1, -1):
        num = int(num) * cont
    print ("\n")
    print ("O fatorial de", fat, "é", num); print ("\n")