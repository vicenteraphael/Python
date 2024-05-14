def msg_adeus():
    print ("\n"); print ("Adeus!")

a = ""
b = ""
c = ""

print ("\nBem-vindo(a) à Calculadora de Juros Simples do Raphael")

# Menu de opções:

while a != "s" and b != "s" and c != "s" and b != "3":
    print ("\n")
    a = ""
    b = ""
    c = ""
    print ("Desejas calcular: \n\n1) Juros (J) e Montante (M) \n2) Capital (C) \n3) Taxa percentual (i) \n4) Tempo em meses (t) \n5) Sair \n\n")
    a = input ()
    while a != "1" and a != "2" and a != "3" and a != "4" and a != "5":
        print ("\n*alternativa inválida*")
        print ("Desejas calcular: \n\n1) Juros e Montante \n2) Capital (C) \n3) Taxa \n4) Tempo \n5) Sair\n\n")
        a = input ()
    if a == "5":
        msg_adeus()
        break

    # Juros (J) e Montante (M):

    while a == "1":
        print ("\n\n*Para sair, entre com 's' \nPara voltar ao Menu de Opções, entre com 'm'* \n\nInforme-me:"); print ("\n")
        while True:
            try:
                a = input ("Capital (C): ")
                if a == "s" or a == "m":
                    break
                else:
                    a = float(a)
                    break
            except ValueError or TypeError:
                print ("Entre com um número!")
        if a == "s":
            msg_adeus()
            break
        elif a != "m":
            while True:
                try:
                    b = input ("Taxa percentual (i): ")
                    if b == "s" or b == "m":
                        break
                    else:
                        b = float(b)
                        break
                except ValueError or TypeError:
                    print ("Entre com um número!")
            if b == "s":
                msg_adeus()
                break
        if a != "m" and  b != "m":
            while True:
                try:
                    c = input ("Tempo em meses (t): ")
                    if c == "s" or c == "m":
                        break
                    else:
                        c = float(c)
                        break
                except ValueError or TypeError:
                    print ("Entre com um número!")
            if c == "s":
                msg_adeus()
                break

        # Cálculo/Resultado:

        if a != "m" and b != "m" and c != "m":

            if a == 0:
                print ("\nNeste momento eu imagino que você esteja sendo investigado pelo FBI e sendo procurado em 17364594 países diferentes. O cara investiu R$ 0,00 e tá querendo lucrar...")
            elif b == 0:
                print ("\nCara, o Palmeiras vai conquistar o mundial e o seu dinheiro não vai render KAKAKAKAKKAKKAKKAKKAKAKAKAKAKA")
            elif c == 0:
                print ("\nPelo visto você é bastante apressado, não? Aqui está o perfeito exemplo do ditado popular 'quem se apressa come cru'...")
            elif a < 0 and b > 0 and c > 0:
                print ("\nO cara endividado e querendo realizar aplicações KAAKKKAKAKKAKA")
            elif b < 0 and a > 0 and c > 0:
                print ("\ntaxa negativa? Se você quer jogar seu dinheiro fora, tudo bem. Agora não me faça perder o meu tempo também...")
            elif c < 0 and a > 0 and b > 0:
                print ("\nCara, não é porque a sua aplicação irá durar menos que um mês que você deva inserir um valor negativo. \nComo eu sou bonzinho, eu vou até te fornecer a fórmula para fazer a conversão -- sendo: \n\nx = o número de dias que a aplicação irá durar; \ny = o número de dias que há no mês da aplicação; \nf(x, y) = o tempo em meses, em função de x e y.\n\n-- f(x, y) = x / y \n\nComo podes notar, o resultado será positivo e decimal. \nVocê deve ter notado, também, que é possível formar um gráfico com os possíveis valores de x... Ahh ... como a matemática é bela... \nMas algo me diz que você inseriu um valor negativo só pra me zoar. Neste caso, saiba que, como programador, eu me senti bastante ofendido :/ VOU TE CANCELAR NO TWITTER HEHHEHHRHARHEHEHTH")
            elif a < 0 or b < 0 or c < 0:
                print ("\nNão seja assim, amigo, é muito vergonhoso aplicar valores negativos no contexto de cálculo de juros...")
            else:
                c = (a * b * c)/100
                a = a + c
                print ("\nJ =", c, "\nM =", a)
            
            # Continuar/Voltar/Sair:

            print ("\n\nDesejas: \n\n1) Continuar \n2) Voltar ao Menu de opções \n3) Sair \n\n")
            b = input ()
            while b != "1" and b != "2" and b != "3":
                print ("\n\n*alternativa inválida*\nDesejas: \n\n1) Continuar \n2) Voltar ao Menu de opções \n3) Sair")
                b = input ()
            if b == "3":
                msg_adeus()
                break
            elif b == "2":
                break
            elif b == "1":
                a = "1"

    # Capital (C):

    while a == "2":
        print ("\n*para sair, entre com 's' \npara voltar ao Menu de opções, entre com 'm'*\n\nVocê prefere calcular a partir do valor de: \n\n1) Juros (J), Taxa (i), Tempo (t)  \n2) Montante (M) e Juros (J)\n\n")
        a = input ("")
        while a != "1" and a != "2" and a != "s" and a != "m":
            print ("\n*alternativa inválida*\n*para sair, entre com 's' \npara voltar ao Menu de opções, entre com 'm'*\nVocê sabe o valor de(o): \n\n1) Juros (J), Taxa (i), Tempo (t)  \n2) Montante \n\n")
            a = input ("")
            if a == "s" or a == "m":
                break
        if a == "s":
            msg_adeus()
        elif a == "m":
            break
        elif a == "1":

            # A partir de: Juros (J) , Taxa (i) e Tempo (t):

            print ("\n\n*para sair, entre com 's' \npara voltar ao Menu de opções, entre com 'm'*\nInforme-me: \n\n")
            while True:
                try:
                    a = input ("Juros (J): ")
                    if a == "s" or a == "m":
                        break
                    else:
                        a = float(a)
                        break
                except ValueError or TypeError:
                    print ("Entre com um número!")
            if a == "s":
                msg_adeus()
                break
            if a != "m":
                while True:
                    try:
                        b = input ("Taxa percentual (i): ")
                        if b == "s" or b == "m":
                            break
                        else:
                            b = float(b)
                            break
                    except ValueError or TypeError:
                        print ("Entre com um número!")
                if b == "s":
                    msg_adeus()
                    break
            if a != "m" and b != "m":
                while True:
                    try:
                        c = input ("Tempo em meses (t): ")
                        if c == "s" or c == "m":
                            break
                        else:
                            c = float(c)
                            break
                    except ValueError or TypeError:
                        print ("Entre com um número!")
                if c == "s":
                    msg_adeus()
                    break
            if a != "m" and b != "m" and c != "m":

                # Cálculo/Resultado:

                if a < 0 or b < 0 or c < 0:
                    print ("\nNão seja assim, amigo, é muito vergonhoso aplicar valores negativos neste contexto...")
                elif c == 0 and a > 0 or b == 0 and a > 0:
                    print ("\nOpa, meu nobre, tentar descobrir o valor do capital sem que o mesmo tenha rendido é como desfazer um trabalho que ainda não foi feito... Os possíveis valores são infinitos!\nAliás, como que você obteu um valor para o juros, de qualquer maneira?")
                elif c == 0 and a == 0 and b > 0:
                    print ("\nOpa, meu nobre, tentar descobrir o valor do capital sem que o mesmo tenha rendido é como desfazer um trabalho que ainda não foi feito... Os possíveis valores são infinitos!")
                elif b == 0 and a > 0:
                    print ("\nInteressante o jeito que você quer que eu calcule o valor de seu capital sem que tinha sido aplicada uma taxa ao mesmo...\nAliás, como que você obteu um valor para o juros, de qualquer maneira?")
                elif a == 0 and b > 0 and c > 0:
                    print ("\nContate o seu advogado! \nOu possivelmente houve um erro grotesco no processo de sua aplicação ou você está me zoando...\nCaso o segundo caso seja verdadeiro, saiba que eu me sinto realmente ofendido... VOU TE CANCELAR NO TWITTER HEHHEHHEHHEHEHEHEHEHEHEHEHEHEH")
                elif a == 0 and b == 0 and c > 0:
                    print ("\nhmmmm... pelo visto, na sua aplicação, você perdeu", c, "mes(es) da sua vida..." )
                elif c > a or b/100 > a:
                    print ("\nVamos a uma pequena ponderação matemática. Se J = (C * i * t) / 100, então, necessáriamente: C < J, i% < J e t < J. Achou que eu ia deixar essa passar, né?")
                elif a == 0 and b == 0 and c == 0:
                    print ("\nOpa, meu nobre, tentar descobrir o valor do capital sem que o mesmo tenha rendido é como desfazer um trabalho que ainda não foi feito... Os possíveis valores são infinitos!")
                else:
                    print ("\nC =", (100 * a) / (b * c))

                # Continuar/Voltar/Sair:

                print ("\nDesejas: \n\n1) Continuar \n2) Voltar ao menu de opções \n3) Sair")
                b = input ("\n")
                while b != "1" and b != "2" and b != "3":
                    print ("*alternativa inválida*")
                    print ("Desejas: \n\n1) Continuar \n2) Voltar ao menu de opções \n3) Sair")
                    b = input ("\n")
                if b == "3":
                    msg_adeus()
                    break
                elif b == "2":
                    break
                elif b == "1":
                    a = "2"

        # A partir de: Montante (M) e Juros (J):

        elif a == "2":
            print ("\nInforme-me:\n")
            while True:
                try:
                    a = input ('Montante (M): ')
                    if a == "s" or a == "m":
                        break
                    else:
                        a = float(a)
                        break
                except ValueError or TypeError:
                    print ("Entre com um número!")
            if a == "s":
                msg_adeus()
                break
            elif a != "m":
                while True:
                    try:
                        b = input ("Juros (J): ")
                        if b == "s" or b == "m":
                            break
                        else:
                            b = float(b)
                            break
                    except ValueError or TypeError:
                        print ("Entre com números!")
                if b == "s":
                    msg_adeus()
                    break
                elif a != "m" and b != "m":

                    # Cálculo/Resultado:

                    if b > a:
                        print ("\nUma pequena ponderação: se M = J + C, então, necessariamente, J < M (exceto o caso em que C = 0, mas isto é um absurdo em tratando-se de cálculo de juros!). Achou que eu ia deixar essa passar, né?")
                    elif b == a:
                        print ("\nBom, vamos a uma dissertação matemática. Sendo M = J + C, o valor para c que satisfaz o caso em que M = J é C = 0 . Agora me diz, que diacho de aplicação foi essa que você fez?")
                    elif a < 0 or b < 0:
                        print ("\nmano, wtf ?")
                    else:
                        print ("\nC =", a - b )

                    # Continuar/Voltar/Sair:

                    print ("\nDesejas: \n\n1) Continuar \n2) Voltar ao menu de opções \n3) Sair")
                    b = input ("\n")
                    while b != "1" and b != "2" and b != "3":
                        print ("*alternativa inválida*")
                        print ("Desejas: \n\n1) Continuar \n2) Voltar ao menu de opções \n3) Sair")
                        b = input ("\n")
                    if b == "3":
                        msg_adeus()
                        break
                    elif b == "2":
                        break
                    elif b == "1":
                        a = "2"
    
    # Taxa percentual (i):

    while a == "3":
        print ("\n*para sair, entre com 's' \npara voltar ao Menu de opções, entre com 'm'*\n\nInforme-me: \n")
        while True:
            try:
                a = input ("Juros (J): ")
                if a == "s" or a == "m":
                    break
                else:
                    a = float(a)
                    break
            except ValueError or TypeError:
                print ("Entre com um número!")
        if a == "s":
            msg_adeus()
            break
        elif a != "m":
            while True:
                try:
                    b = input ("Capital (C): ")
                    if b == "s" or b == "m":
                        break
                    else:
                        b = float(b)
                        break
                except ValueError or TypeError:
                    print ("Entre com um número!")
            if b == "s":
                msg_adeus()
                break
            elif a != "m" and b != "m":
                while True:
                    try:
                        c = input ("Tempo (t) em meses: ")
                        if c == "s" or c == "m":
                            break
                        else:
                            c = float(c)
                            break
                    except ValueError or TypeError:
                        print ("Entre com um número!")
                if c == "s":
                    msg_adeus()
                    break
                if a != "m" and b != "m" and c != "m":

                    # Cálculo/Resultado:
                    if a > 0 and b > a or a > 0 and c > a:
                        print ("\nVamos a uma pequena ponderação matemática. Se J = (C * i * t) / 100, então, necessáriamente: C < J, i% < J e t < J. Achou que eu ia deixar essa passar, né?")
                    elif a < 0 or b < 0 or c < 0:
                        print ("\nNão seja assim, amigo, é muito vergonhoso aplicar valores negativos neste contexto...")
                    elif a == 0 and b > 0 and c > 0:
                        print ("\nMoço(a), sugiro que você contate o seu advogado, seu dinheiro não rendeu :/")
                    elif b == 0 and c > a and a == 0:
                        print ("\nNão me faça rir. Aplicar R$ 0,00 e isto ter rendido alguma coisa é história para boi dormir... perdão, quase peguei no sono... Não, pera!")
                    elif b == 0 and c >= a and a > 0:
                        print ("\nNão me faça rir. Aplicar R$ 0,00 e isto ter rendido alguma coisa é história para boi dormir...\nAliás, que tipo de droga você consumiu para obter", a, "como valor para o juros?")
                    elif b == 0 and a == 0 and c == 0:
                        print ("\nAmigo, os valores possíveis para a taxa desta sua aplicação são infinitos!")
                    elif a == 0 and b == 0 and c > 0:
                        print ("\nhmmmm... pelo visto, na sua aplicação, você perdeu", c, "mes(es) da sua vida..." )
                    elif c == 0 and a == 0:
                        print ("\nPaciência, amigo, querer que o dinheiro renda instantâneamente é como querer que caia do céu uma figurinha do Neymar... \nInvista um pouco mais de tempo, depois venha falar comigo...")
                    elif c == 0 and a > 0:
                        print ("\nPaciência, amigo, querer que o dinheiro renda instantâneamente é como querer que caia do céu uma figurinha do Neymar... \nInvista um pouco mais de tempo, depois venha falar comigo...\nAliás, que tipo de droga você consumiu para obter", a, "como valor para o juros?")
                    else:
                        print ("\ni =", a * 100 / (b * c), "(%)")

                    # Continuar/Voltar/Sair:

                    print ("\nDesejas: \n\n1) Continuar \n2) Voltar ao menu de opções \n3) Sair")
                    b = input ("\n")
                    while b != "1" and b != "2" and b != "3":
                        print ("*alternativa inválida*")
                        print ("Desejas: \n\n1) Continuar \n2) Voltar ao menu de opções \n3) Sair")
                        b = input ("\n")
                    if b == "3":
                        msg_adeus()
                        break
                    elif b == "2":
                        break
                    elif b == "1":
                        a = "3"

    # Tempo (t) em meses:

    while a == "4":
        print ("\n*para sair, entre com 's' \npara voltar ao Menu de opções, entre com 'm'*\n\nInforme-me: \n")
        while True:
            try:
                a = input ("Juros (J): ")
                if a == "s" or a == "m":
                    break
                else:
                    a = float(a)
                    break
            except ValueError or TypeError:
                print ("Entre com um número!")
        if a == "s":
            msg_adeus()
            break
        elif a != "m":
            while True:
                try:
                    b = input ("Capital (C): ")
                    if b == "s" or b == "m":
                        break
                    else:
                        b = float(b)
                        break
                except ValueError or TypeError:
                    print ("Entre com um número!")
            if b == "s":
                msg_adeus()
                break
            elif a != "m" and b != "m":
                while True:
                    try:
                        c = input ("Taxa percentual (i): ")
                        if c == "s" or c == "m":
                            break
                        else:
                            c = float(c)
                            break
                    except ValueError or TypeError:
                        print ("Entre com um número!")
                if c == "s":
                    msg_adeus()
                    break
                elif a != "m" and b != "m" and c != "m":

                    # Cálculo/Resultado:
                    if c == 0 and a > 0:
                        print ("\nNão me faça rir. Aplicar uma taxa de 0% e o dinheiro ter rendido alguma coisa é história para boi dormir... Perdão! Quase peguei no sono... Não, pera!")
                    elif c == 0 and a == 0:
                        print ("\nRapaz, os valores possíveis para o tempo de sua aplicação são infinitos!")
                    elif b > a or c/100 > a:
                        print ("\nVamos a uma pequena ponderação matemática. Se J = (C * i * t) / 100, então, necessáriamente: C < J, i% < J e t < J. Achou que eu ia deixar essa passar, né?")
                    elif a < 0 or b < 0 or c < 0:
                        print ("\nNão seja assim, amigo, é vergonhoso aplicar valores negativos neste contexto...")
                    else:
                        print ("\nt =", a * 100 / (b * c), "mes(es)")

                    # Continuar/Voltar/Sair:

                    print ("\nDesejas: \n\n1) Continuar \n2) Voltar ao menu de opções \n3) Sair")
                    b = input ("\n")
                    while b != "1" and b != "2" and b != "3":
                        print ("*alternativa inválida*")
                        print ("Desejas: \n\n1) Continuar \n2) Voltar ao menu de opções \n3) Sair")
                        b = input ("\n")
                    if b == "3":
                        msg_adeus()
                        break
                    elif b == "2":
                        break
                    elif b == "1":
                        a = "4"