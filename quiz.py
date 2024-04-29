print ("\n")
print ("Bem-vindo ao Trivia Quiz do Raphael"); print ("\n")
a = 0
e = 0
op = ""
while op != "s":
    print ("Para iniciar, digite 'i'. \nPara sair, digite 's'"); print ("\n")
    op = input ()
    while op != "s" and op != "i":
        print ("\n")
        print ("*escolha inválida*")
        op = input ()
        if op == "s":
            print ("\n")
            print ("Adeus!")
            break
    if op == "s":
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
            e = e + 1
        case "b":
            a = a + 1
        case "c":
            e = e + 1
        case "d":
            e = e + 1
    print ("\n")
    print ("2. Quem nasce no Rio Grande do Norte é:"); print ("\n")
    print ("a) Rio Grandense \nb) Rio Grande do Norteiro \nc) Potiguar \nd) Rio Grandista do Norte"); print ("\n")
    r2 = input ()
    while r2 != "a" and r2 != "b" and r2 != "c" and r2 != "d":
        print ("\n")
        print ("*alternativa inválida* \n2. Quem nasce no Rio Grande do Norte é:"); print ("\n")
        print ("a) Rio Grandense \nb) Rio Grande do Norteiro \nc) Potiguar \nd) Rio Grandista do Norte"); print ("\n")
        r2 = input ()
    match r2:
        case "a":
            e = e + 1
        case "b":
            e = e + 1
        case "c":
            a = a + 1
        case "d":
            e = e + 1
    print ("\n")
    print ("3. Qual o resultado da expressão 2 - (2 - 2) * 4?"); print ("\n")
    print ("a) - 8 \nb) 0 \nc) 8 \nd) 2")
    r3 = input ()
    while r3 != "a" and r3 != "b" and r3 != "c" and r3 != "d":
        print ("\n")
        print ("*alternativa inválida* \n3. Qual o resultado da expressão 2 - (2 - 2) * 4 ?"); print ("\n")
        print ("a) - 8 \nb) 0 \nc) 8 \nd) 2"); print ("\n")
        r3 = input ()
    match r3:
        case "a":
            e = e + 1
        case "b":
            e = e + 1
        case "c":
            a = a + 1
        case "d":
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
            a = a + 1
        case "b":
            e = e + 1
        case "c":
            e = e + 1
        case "d":
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
            e = e + 1
        case "b":
            e = e + 1
        case "c":
            a = a + 1
        case "d":
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
            e = e + 1
        case "b":
            e = e + 1
        case "c":
            a = a + 1
        case "d":
            e = e + 1