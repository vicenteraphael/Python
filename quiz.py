print ("\n")
print ("Bem-vindo ao Trivia Quiz do Raphael"); print ("\n")
r1 = ""
while r1 != "s":
    a = 0
    e = 0
    print ("Para iniciar, digite 'i'. \nPara sair, digite 's'"); print ("\n")
    r1 = input ()
    while r1 != "s" and r1 != "i":
        print ("\n")
        print ("*escolha inválida* \nPara iniciar, digite 'i'. \nPara sair, digite 's'"); print ("\n")
        r1 = input ()
        if r1 == "s":
            break
    if r1 == "s":
        print ("\n")
        print ("Adeus!")
        break
    print ("\n")
    print ("1. Qual o plural da palavra 'qualquer'?"); print ("\n")
    print ("a) quaisqueres \nb) quaisquer \nc) qualqueres \nd) não existe"); print ("\n")
    r1 = input ()
    while r1 != "a" and r1 != "b" and r1 != "c" and r1 != "d":
        print ("\n")
        print ("*alternativa inválida* \n1. Qual o plural da palavra 'qualquer'?"); print ("\n")
        print ("a) quaisqueres \nb) quaisquer \nc) qualqueres \nd) não existe"); print ("\n")
        r1 = input ()
    match r1:
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
    print ("\n")
    print ("2. Quem nasce no Rio Grande do Norte é:"); print ("\n")
    print ("a) Rio Grandense Nortista \nb) Rio Grande do Norteiro \nc) Potiguar \nd) Rio Grandista do Norte"); print ("\n")
    r2 = input ()
    while r2 != "a" and r2 != "b" and r2 != "c" and r2 != "d":
        print ("\n")
        print ("*alternativa inválida* \n2. Quem nasce no Rio Grande do Norte é:"); print ("\n")
        print ("a) Rio Grandense Nortista \nb) Rio Grande do Norteiro \nc) Potiguar \nd) Rio Grandista do Norte"); print ("\n")
        r2 = input ()
    match r2:
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
    print ("\n")
    print ("3. Qual o resultado da expressão 2 - (2 - 2) * 4?"); print ("\n")
    print ("a) - 8 \nb) 0 \nc) 8 \nd) 2"); print ("\n")
    r3 = input ()
    while r3 != "a" and r3 != "b" and r3 != "c" and r3 != "d":
        print ("\n")
        print ("*alternativa inválida* \n3. Qual o resultado da expressão 2 - (2 - 2) * 4 ?"); print ("\n")
        print ("a) - 8 \nb) 0 \nc) 8 \nd) 2"); print ("\n")
        r3 = input ()
    match r3:
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
    print ("\n")
    print ("4. Qual dos países a seguir não é da Europa?"); print ("\n")
    print ("a) Egito \nb) Grécia \nc) Hungria \nd) Polônia"); print ("\n")
    r4 = input ()
    while r4 != "a" and r4 != "b" and r4 != "c" and r4 != "d":
        print ("\n")
        print ("*alternativa inválida* \n4. Qual dos países a seguir NÃO é da Europa?"); print ("\n")
        print ("a) Egito \nb) Grécia \nc) Hungria \nd) Polônia"); print ("\n")
        r4 = input ()
    match r4:
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
    print ("\n")
    print ("5. A palavra 'inadvertidamente' é um(a):"); print ("\n")
    print ("a) verbo \nb) preposição \nc) advérbio \nd) interjeição"); print ("\n")
    r5 = input ()
    while r5 != "a" and r5 != "b" and r5 != "c" and r5 != "d":
        print ("\n")
        print ("*alternativa inválida* \n5. A palavra 'inadvertidamente' é um(a):"); print ("\n")
        print ("a) verbo \nb) preposição \nc) advérbio \nd) interjeição"); print ("\n")
        r5 = input ()
    match r5:
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
    print ("\n")
    print ("6. O número 293.45 pertence ao conjunto dos números:"); print ("\n")
    print ("a) Racionais \nb) Inteiros \nc) Irracionais \nd) Naturais"); print ("\n")
    r6 = input ()
    while r6 != "a" and r6 != "b" and r6 != "c" and r6 != "d":
        print ("\n")
        print ("*alternativa inválida* \n6. O número 293.45 pertence ao conjunto dos números:"); print ("\n")
        print ("a) Racionais \nb) Inteiros \nc) Irracionais \nd) Naturais"); print ("\n")
        r6 = input ()
    match r6:
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
    print ("\n")
    print ("7. Regime político no qual o rei possui total poder:"); print ("\n")
    print ("a) Democracia \nb) Absolutismo \nc) Anarquismo \nd) Comunismo"); print ("\n")
    r7 = input ()
    while r7 != "a" and r7 != "b" and r7 != "c" and r7 != "d":
        print ("\n")
        print ("*alternativa inválida* \n7. Regime político em que o rei possui total poder:"); print ("\n")
        print ("a) Democracia \nb) Absolutismo \nc) Anarquismo \nd) Comunismo"); print ("\n")
        r7 = input ()
    match r7:
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
    print ("\n")
    print ("8. No dia 21 de abril comemora-se:"); print ("\n")
    print ("a) Dia de Tiradentes \nb) Páscoa \nc) Dia do Trabalho \nd) Carnaval"); print ("\n")
    r8 = input ()
    while r8 != "a" and r8 != "b" and r8 != "c" and r8 != "d":
        print ("\n")
        print ("8. No dia 21 de abril comemora-se:"); print ("\n"); print ("\n")
        print ("a) Dia de Tiradentes \nb) Páscoa \nc) Dia do Trabalho \nd) Carnaval"); print ("\n")
        r8 = input ()
    match r8:
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
    print ("\n")
    print ("9. Qual figura de linguagem predominante no ditado popular: 'Água mole. Pedra dura. Tanto bate até que fura'?"); print ("\n")
    print ("a) Antítese \nb) Metonímia \nc) Metáfora \nd) Prosopopéia"); print ("\n")
    r9 = input ()
    while r9 != "a" and r9 != "b" and r9 != "c" and r9 != "d":
        print ("\n")
        print ("*alternativa inválida* \n9. Qual figura de linguagem predominante no ditado popular: 'Água mole. Pedra dura. Tanto bate até que fura'?"); print ("\n")
        print ("a) Antítese \nb) Metonímia \nc) Metáfora \nd) Prosopopéia"); print ("\n")
        r9 = input ()
    match r9:
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
    print ("\n")
    print ("10. De quantas maneiras podemos arranjar uma fila de 4 pessoas?"); print ("\n")
    print ("a) 16 \nb) 8 \nc) 12 \nd) 24"); print ("\n")
    r10 = input ()
    while r10 != "a" and r10 != "b" and r10 != "c" and r10 != "d":
        print ("\n")
        print ("*alternativa inválida* \n10. De quantas maneiras podemos arranjar uma fila de 4 pessoas?"); print ("\n")
        print ("a) 16 \nb) 8 \nc) 12 \nd) 24"); print ("\n")
        r10 = input ()
    match r10:
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
    print ("\n")
    print ("RESULTADOS:"); print ("\n"); print ("Acertos:", a, "\nErros:", e); print ("\n")
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
    print ("Desejas ver o gabarito?"); print ("\n"); print ("1) Sim \n2) Não"); print ("\n")
    r1 = input ()
    while r1 != "1" and r1 != "2":
        print ("\n")
        print ("*resposta inválida* \nDesejas ver o gabarito?"); print ("\n"); print ("1) Sim \n2) Não"); print ("\n")
        r1 = input ()
    if r1 == "1":
        print ("\n")
        print ("1. b)     4. a)      7. b) \n2. c)     5. c)     8. a)     10. d) \n3. c)     6. a)     9. a)")
    print ("\n")
    print ("Desejas voltar ao início ou sair?"); print ("\n"); print ("1) Voltar ao início \n2) Sair"); print ("\n")
    r1 = input (); print ("\n")
    while r1 != "1" and r1 != "2":
        print ("*resposta inválida* \nDesejas voltar ao início ou sair?"); print ("\n"); print ("1) Voltar ao início \n2) Sair"); print ("\n")
        r1 = input ()
        if r1 == "2":
            break
    if r1 == "2":
        print ("Adeus!"); print ("\n")
        break