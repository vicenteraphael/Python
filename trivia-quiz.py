"""
Variáveis:
a = acertos
e = erros
r = variável resposta
"""

#Funções:

def question1():
    print ("1. Qual o plural da palavra 'qualquer'?\n")
    print ("a) quaisqueres \nb) quaisquer \nc) qualqueres \nd) não existe\n")
def question2():
    print ("2. Quem nasce no Rio Grande do Norte é:\n")
    print ("a) Rio Grandense Nortista \nb) Rio Grande do Norteiro \nc) Potiguar \nd) Rio Grandista do Norte\n")
def question3():
    print ("3. Qual o resultado da expressão 2 - (2 - 2) * 4?\n")
    print ("a) - 8 \nb) 0 \nc) 8 \nd) 2\n")
def question4():
    print ("4. Qual dos países a seguir NÃO é da Europa?\n")
    print ("a) Egito \nb) Grécia \nc) Hungria \nd) Polônia\n")
def question5():
    print ("5. A palavra 'inadvertidamente' é um(a):\n")
    print ("a) verbo \nb) preposição \nc) advérbio \nd) interjeição\n")
def question6():
    print ("6. O número 293.45 pertence ao conjunto dos números:\n")
    print ("a) Inteiros \nb) Racionais \nc) Irracionais \nd) Naturais\n")
def question7():
    print ("7. Regime político no qual o rei possui total poder:\n")
    print ("a) Democracia \nb) Absolutismo \nc) Anarquismo \nd) Comunismo\n")
def question8():
    print ("8. No dia 21 de abril comemora-se:\n")
    print ("a) Carnaval \nb) Páscoa \nc) Dia do Trabalho \nd) Dia de Tiradentes \n")
def question9():
    print ("9. Qual figura de linguagem predominante no ditado popular: 'Água mole em pedra dura, tanto bate até que fura'?\n")
    print ("a) Antítese \nb) Metonímia \nc) Metáfora \nd) Prosopopéia\n")
def question10():
    print ("10. De quantas maneiras podemos organizar uma fila de 4 pessoas?\n")
    print ("a) 16 \nb) 8 \nc) 12 \nd) 24\n")
def msg_erro():
    print ("\n*alternativa inválida*")

r = ""
while r != "s":

    #Menu Inicial:

    a = 0
    e = 0

    print ("\nBem-vindo(a) ao Trivia Quiz do Raphael\n")
    print ("Para iniciar, pressione 'Enter'\nPara sair, digite 's'\n")
    r = input ()
    if r == "s":
        break
    
    #Pergunta 1:

    print ("\n")
    question1()
    r = input ()
    while r != "a" and r != "b" and r != "c" and r != "d":
        msg_erro(); question1()
        r = input ()
    match r:
        case "a":
            print ("errado ;-;")
            e = e + 1
        case "b":
            print ("Correto!")
            a = a + 1
        case "c":
            print ("errado ;-;")
            e = e + 1
        case "d":
            print ("errado ;-;")
            e = e + 1
    r = input("Pressione 'Enter' para continuar: ")

    #Pergunta 2:

    print ("\n")
    question2()
    r = input ()
    while r != "a" and r != "b" and r != "c" and r != "d":
        msg_erro(); question2()
        r = input ()
    match r:
        case "a":
            print ("errado ;-;")
            e = e + 1
        case "b":
            print ("errado ;-;")
            e = e + 1
        case "c":
            print ("Correto!")
            a = a + 1
        case "d":
            print ("errado ;-;")
            e = e + 1
    r = input("Pressione 'Enter' para continuar: ")

    #Pergunta 3:

    print ("\n")
    question3()
    r = input ()
    while r != "a" and r != "b" and r != "c" and r != "d":
        msg_erro(); question3()
        r = input ()
    match r:
        case "a":
            print ("errado ;-;")
            e = e + 1
        case "b":
            print ("errado ;-;")
            e = e + 1
        case "c":
            print ("errado ;-;")
            e = e + 1
        case "d":
            print ("Correto!")
            a = a + 1
    r = input("Pressione 'Enter' para continuar: ")

    #Pergunta 4:

    print ("\n")
    question4()
    r = input ()
    while r != "a" and r != "b" and r != "c" and r != "d":
        msg_erro(); question4()
        r = input ()
    match r:
        case "a":
            print ("Correto!")
            a = a + 1
        case "b":
            print ("errado ;-;")
            e = e + 1
        case "c":
            print ("errado ;-;")
            e = e + 1
        case "d":
            print ("errado ;-;")
            e = e + 1
    r = input("Pressione 'Enter' para continuar: ")

    #Pergunta 5:
    
    print ("\n")
    question5()
    r = input ()
    while r != "a" and r != "b" and r != "c" and r != "d":
        msg_erro(); question5()
        r = input ()
    match r:
        case "a":
            print ("errado ;-;")
            e = e + 1
        case "b":
            print ("errado ;-;")
            e = e + 1
        case "c":
            print ("Correto!")
            a = a + 1
        case "d":
            print ("errado ;-;")
            e = e + 1
    r = input("Pressione 'Enter' para continuar: ")

    #Pergunta 6:

    print ("\n")
    question6()
    r = input ()
    while r != "a" and r != "b" and r != "c" and r != "d":
        msg_erro(); question6()
        r = input ()
    match r:
        case "a":
            print ("errado ;-;")
            e = e + 1
        case "b":
            print ("Correto!")
            a = a + 1
        case "c":
            print ("errado ;-;")
            e = e + 1
        case "d":
            print ("errado ;-;")
            e = e + 1
    r = input("Pressione 'Enter' para continuar: ")

    #Pergunta 7:

    print ("\n")
    question7()
    r = input ()
    while r != "a" and r != "b" and r != "c" and r != "d":
        msg_erro(); question7()
        r = input ()
    match r:
        case "a":
            print ("errado ;-;")
            e = e + 1
        case "b":
            print ("Correto!")
            a = a + 1
        case "c":
            print ("errado ;-;")
            e = e + 1
        case "d":
            print ("errado ;-;")
            e = e + 1
    r = input("Pressione 'Enter' para continuar: ")

    #Pergunta 8:

    print ("\n")
    question8()
    r = input ()
    while r != "a" and r != "b" and r != "c" and r != "d":
        msg_erro(); question8()
        r = input ()
    match r:
        case "a":
            print ("errado ;-;")
            e = e + 1
        case "b":
            print ("errado ;-;")
            e = e + 1
        case "c":
            print ("errado ;-;")
            e = e + 1
        case "d":
            print ("Correto!")
            a = a + 1
    r = input("Pressione 'Enter' para continuar: ")

    #Pergunta 9:

    print ("\n")
    question9()
    r = input ()
    while r != "a" and r != "b" and r != "c" and r != "d":
        msg_erro(); question9()
        r = input ()
    match r:
        case "a":
            print ("Correto!")
            a = a + 1
        case "b":
            print ("errado ;-;")
            e = e + 1
        case "c":
            print ("errado ;-;")
            e = e + 1
        case "d":
            print ("errado ;-;")
            e = e + 1
    r = input("Pressione 'Enter' para continuar: ")

    #Pergunta 10:

    print ("\n")
    question10()
    r = input ()
    while r != "a" and r != "b" and r != "c" and r != "d":
        msg_erro; question10()
        r = input ()
    match r:
        case "a":
            print ("errado ;-;")
            e = e + 1
        case "b":
            print ("errado ;-;")
            e = e + 1
        case "c":
            print ("errado ;-;")
            e = e + 1
        case "d":
            print ("Correto!")
            a = a + 1
    r = input("Pressione 'Enter' para ver seus resultados: ")

    #Resultado e ponderações:

    print ("\n")
    print ("RESULTADOS:\n"); print ("Acertos:", a, "\nErros:", e); print ("\n")
    if a <= 2 and a >= 1:
        print ("Você precisa melhorar!!")
    elif a <= 4 and a >= 3:
        print ("Você foi ruim!")
    elif a == 0:
        print ("Ou você está zoando comigo ou você precisa cuidar do seu aprendizado!")
    elif a == 5 or a == 6:
        print ("Tá na média, né? Mas dá pra melhorar...")
    elif a <= 8 and a >= 7:
        print ("Você foi ótimo!")
    elif a == 9:
        print ("Quase perfeito!")
    else:
        print ("Parabéns! Excelente!")
    print ("\n")
    r = input("Pressione 'Enter' para continuar: ")
    print ("\n"); print ("\n")

    #Gabarito:

    print ("\n")
    print ("Desejas ver o gabarito?"); print ("\n"); print ("1) Sim \n2) Não"); print ("\n"); print ("\n")
    r = input ()
    while r != "1" and r != "2":
        print ("\n")
        print ("*resposta inválida* \nDesejas ver o gabarito?"); print ("\n"); print ("1) Sim \n2) Não"); print ("\n")
        r = input ()
    if r == "1":
        print ("\n")
        print ("1. b)     4. a)     7. b) \n2. c)     5. c)     8. d)     10. d) \n3. d)     6. b)     9. a)")
    print ("\n")
    r = input("Pressione 'Enter' para continuar: "); print ("\n")
    print ("\n")

    #Voltar ao Início ou Sair:

    print ("Desejas voltar ao início ou sair?"); print ("\n"); print ("1) Voltar ao início \n2) Sair"); print ("\n")
    r = input (); print ("\n")
    while r != "1" and r != "2":
        print ("*resposta inválida* \nDesejas voltar ao início ou sair?"); print ("\n"); print ("1) Voltar ao início \n2) Sair"); print ("\n")
        r = input ()
        if r == "2":
            break
    if r == "2":
        print ("Adeus!"); print ("\n")
        break
    if r == "1":
        print ("\n"); print ("\n")