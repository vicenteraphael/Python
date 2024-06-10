a = ""
b = ""
c = ""

print ("\nBem-vindo(a) à Calculadora de Juros Simples do Raphael")

# Menu de opções:

while a != "s" and b != "s" and c != "s" and b != "3":
    print ("\nDesejas calcular: \n\n1) Juros (J) e Montante (M) \n2) Capital (C) \n3) Taxa percentual (i) \n4) Tempo em meses (t) \n5) Sair\n")
    a = input ()
    while a != "1" and a != "2" and a != "3" and a != "4" and a != "5":
        print ("*alternativa inválida*")
        print ("Desejas calcular: \n\n1) Juros e Montante \n2) Capital (C) \n3) Taxa \n4) Tempo \n5) Sair\n")
        a = input ()
    if a == "5":        
        break

    # Juros (J) e Montante (M):

    while a == "1":
        print ("\n\n*Para sair, entre com 's' \nPara voltar ao Menu de Opções, entre com 'm'* \n\nInforme-me:"); print ("\n")
        while True:
            try:
                a = input ("Capital (C): ")
                if a == "s" or a == "m":
                    break
                a = float(a)
                break
            except ValueError or TypeError:
                print ("Entre com um número!")
        if a == "s" or a == "m":            
            break
        while True:
            try:
                b = input ("Taxa percentual (i): ")
                if b == "s" or b == "m":
                    break
                b = float(b)
                break
            except ValueError or TypeError:
                print ("Entre com um número!")
        if b == "s" or b == "m":                
            break
        while True:
            try:
                c = input ("Tempo em meses (t): ")
                if c == "s" or c == "m":
                    break
                c = float(c)
                break
            except ValueError or TypeError:
                print ("Entre com um número!")
        if c == "s" or c == "m":                
            break

        # Cálculo/Resultado:

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
            print ("\nCara, não é porque a sua aplicação irá durar menos que um mês que você deva inserir um valor negativo. \nComo eu sou bonzinho, eu vou até te fornecer a fórmula para fazer a conversão -- sendo: \n\nx = o número de dias que a aplicação irá durar; \ny = o número de dias que há no mês da aplicação; \nf(x, y) = o tempo em meses, em função de x e y.\n\n-- f(x, y) = x / y \n\nComo podes notar, o resultado será positivo e decimal. \nVocê deve ter notado, também, que é possível formar um gráfico com os possíveis valores de x e y... Ahh ... como a matemática é bela... \nMas algo me diz que você inseriu um valor negativo só pra me zoar. Neste caso, saiba que, como programador, eu me senti bastante ofendido :/ VOU TE CANCELAR NO TWITTER HEHHEHHRHARHEHEHTH")
        elif a < 0 or b < 0 or c < 0:
            print ("\nNão seja assim, amigo, é muito vergonhoso aplicar valores negativos no contexto de cálculo de juros...")
        else:
            try:
                c = (a * b * c)/100
                a = a + c
                print ("\nJ =", c, "\nM =", a)
            except OverflowError:
                print ("\nPor favor, caro usuário. Não insira valores estrondosos, pois excede o limite de caracteres suportado ;)")
        
        # Continuar/Voltar/Sair:

        print ("\nDesejas: \n\n1) Continuar \n2) Voltar ao Menu de opções \n3) Sair \n")
        b = input ()
        while b != "1" and b != "2" and b != "3":
            print ("*alternativa inválida* \nDesejas: \n\n1) Continuar \n2) Voltar ao Menu de opções \n3) Sair")
            b = input ()
        if b == "3" or b == "2":                
            break
        elif b == "1":
            a = "1"

    # Capital (C):

    while a == "2":
        print ("\n*para sair, entre com 's'. Para voltar ao Menu de opções, entre com 'm'*\n\nVocê prefere calcular a partir do valor de: \n\n1) Juros (J), Taxa (i), Tempo (t)  \n2) Montante (M) e Juros (J)\n")
        a = input ("")
        while a != "1" and a != "2" and a != "s" and a != "m":
            print ("\n*alternativa inválida*\n*para sair, entre com 's'. Para voltar ao Menu de opções, entre com 'm'*\nVocê sabe o valor de(o): \n\n1) Juros (J), Taxa (i), Tempo (t)  \n2) Montante \n")
            a = input ("")
            if a == "s" or a == "m":
                break
        if a == "s" or a == "m":
            break            
        elif a == "1":

            # A partir de: Juros (J) , Taxa (i) e Tempo (t):

            print ("\n*para sair, entre com 's' \npara voltar ao Menu de opções, entre com 'm'*\nInforme-me:\n")
            while True:
                try:
                    a = input ("Juros (J): ")
                    if a == "s" or a == "m":
                        break
                    a = float(a)
                    break
                except ValueError or TypeError:
                    print ("Entre com um número!")
            if a == "s" or a == "m":                
                break
            while True:
                try:
                    b = input ("Taxa percentual (i): ")
                    if b == "s" or b == "m":
                        break
                    b = float(b)
                    break
                except ValueError or TypeError:
                    print ("Entre com um número!")
            if b == "s" or b == "m":                    
                break
            while True:
                try:
                    c = input ("Tempo em meses (t): ")
                    if c == "s" or c == "m":
                        break
                    c = float(c)
                    break
                except ValueError or TypeError:
                    print ("Entre com um número!")
            if c == "s" or c == "m":                    
                break

            # Cálculo/Resultado:

            if a < 0 or b < 0 or c < 0:
                print ("\nNão seja assim, amigo, é muito vergonhoso aplicar valores negativos neste contexto...")
            elif c == 0 and a > 0 or b == 0 and a > 0:
                print ("\nOpa, meu nobre, tentar descobrir o valor do capital sem que o mesmo tenha rendido é como desfazer um trabalho que ainda não foi feito...\nAliás, como que você obteu um valor para o juros, de qualquer maneira?")
            elif c == 0 and a == 0 and b > 0:
                print ("\nOpa, meu nobre, tentar descobrir o valor do capital sem que o mesmo tenha rendido é como desfazer um trabalho que ainda não foi feito... Os possíveis valores são infinitos!")
            elif b == 0 and a > 0:
                print ("\nInteressante o jeito que você quer que eu calcule o valor de seu capital sem que tinha sido aplicada uma taxa ao mesmo...\nAliás, como que você obteu um valor para o juros, de qualquer maneira?")
            elif a == 0 and b > 0 and c > 0:
                print ("\nContate o seu advogado! \nOu possivelmente houve um erro grotesco no processo da sua aplicação ou você está me zoando...\nCaso o segundo caso seja verdadeiro, saiba que eu me sinto realmente ofendido... VOU TE CANCELAR NO TWITTER HEHHEHHEHHEHEHEHEHEHEHEHEHEHEH")
            elif a == 0 and b == 0 and c > 0:
                print ("\nhmmmm... pelo visto, na sua aplicação, você perderá", c, "mes(es) da sua vida..." )

            elif a == 0 and b == 0 and c == 0:
                print ("\nOpa, meu nobre, tentar descobrir o valor do capital sem que o mesmo tenha rendido é como desfazer um trabalho que ainda não foi feito... Os possíveis valores são infinitos!")
            else:
                try:
                    print ("\nC =", (100 * a) / (b * c))
                except OverflowError:
                    print ("\nPor favor, caro usuário. Não insira valores estrondosos, pois excede o limite de caracteres suportado ;)")

            # Continuar/Voltar/Sair:

            print ("\nDesejas: \n\n1) Continuar \n2) Voltar ao menu de opções \n3) Sair")
            b = input ("\n")
            while b != "1" and b != "2" and b != "3":
                print ("*alternativa inválida*")
                print ("Desejas: \n\n1) Continuar \n2) Voltar ao menu de opções \n3) Sair")
                b = input ("\n")
            if b == "3" or b == "2":                    
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
                    a = float(a)
                    break
                except ValueError or TypeError:
                    print ("Entre com um número!")
            if a == "s" or a == "m":                
                break
            while True:
                try:
                    b = input ("Juros (J): ")
                    if b == "s" or b == "m":
                        break
                    b = float(b)
                    break
                except ValueError or TypeError:
                    print ("Entre com números!")
            if b == "s" or b == "m":                    
                break

            # Cálculo/Resultado:

            if a < 0 or b < 0:
                print ("\nNão seja assim, amigo, inserir valores negativos neste contexto é muito vergonhoso...")
            elif b > a or b == a:
                print ("\nUma pequena ponderação matemática: se M = J + C, então, necessariamente, J < M e C < M (exceto o caso em que J = 0 e/ou C = 0 e, então, M = J e/ou M = C, respectivamente. mas isto é um absurdo em tratando-se de cálculo de juros!). Achou que eu ia deixar essa passar, né?")
            elif b == a:
                print ("\nBom, vamos a uma dissertação matemática. Sendo M = J + C e todos os valores são números reais positivos, logicamente. \no valor para c que satisfaz o caso em que M = J é C = 0 . Agora me diz, que diacho de aplicação foi essa que você fez?")
            else:
                try:
                    print ("\nC =", a - b)
                except OverflowError:
                    print ("\nPor favor, caro usuário. Não insira valores estrondosos, pois excede o limite de caracteres suportado ;)")

            # Continuar/Voltar/Sair:

            print ("\nDesejas: \n\n1) Continuar \n2) Voltar ao menu de opções \n3) Sair")
            b = input ("\n")
            while b != "1" and b != "2" and b != "3":
                print ("*alternativa inválida*")
                print ("Desejas: \n\n1) Continuar \n2) Voltar ao menu de opções \n3) Sair")
                b = input ("\n")
            if b == "3" or b == "2":                        
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
                a = float(a)
                break
            except ValueError or TypeError:
                print ("Entre com um número!")
        if a == "s" or a == "m":            
            break
        elif a != "m":
            while True:
                try:
                    b = input ("Capital (C): ")
                    if b == "s" or b == "m":
                        break
                    b = float(b)
                    break
                except ValueError or TypeError:
                    print ("Entre com um número!")
            if b == "s" or b == "m":                
                break
            while True:
                try:
                    c = input ("Tempo (t) em meses: ")
                    if c == "s" or c == "m":
                        break
                    c = float(c)
                    break
                except ValueError or TypeError:
                    print ("Entre com um número!")
            if c == "s" or c == "m":                    
                break

            # Cálculo/Resultado:

            if a < 0 or b < 0 or c < 0:
                print ("\nNão seja assim, amigo, é muito vergonhoso aplicar valores negativos neste contexto...")
            elif a == 0 and b > 0 and c > 0:
                print ("\nhmmmm... então quer dizer que você aplicou", b, "R$ e perdeu", c, "mes(es da sua vida... e ainda veio conferir se isto estava certo... taxa 0...)")
            elif b == 0 and c > a and a == 0:
                print ("\nEspera... é muita coisa pra eu processar... Você aplicou R$ 0,00... esperou por", c, "mes(es)... E ainda queria que isso tivesse rendido alguma coisa!? \nE AGORA TÁ CHECANDO PRA VER SE NÃO FOI ENGANADO...")
            elif b == 0 and c >= a and a > 0:
                print ("\nNão me faça rir. Aplicar R$ 0,00 e isto ter rendido alguma coisa é história para boi dormir...perdão, quase peguei no sono... Não, pera!?")
            elif b == 0 and a == 0 and c == 0:
                print ("\nAmigo, os valores possíveis para a taxa desta sua aplicação são infinitos!")
            elif a == 0 and b == 0 and c > 0:
                print ("\nhmmmm... pelo visto, na sua aplicação, você perderá", c, "mes(es) da sua vida e", b, "R$ do seu bolso...")
            elif c == 0 and a == 0:
                print ("\nPaciência, amigo, querer que o dinheiro renda instantâneamente é como querer que caia do céu uma figurinha do Neymar... \nInvista um pouco mais de tempo, depois venha falar comigo...")
            elif c == 0 and a > 0:
                print ("\nPaciência, amigo, querer que o dinheiro renda instantâneamente é como querer que caia do céu uma figurinha do Neymar... \nInvista um pouco mais de tempo, depois venha falar comigo...\nAliás, que tipo de droga você consumiu para obter", a, "como valor para o juros?")
            else:
                try:
                    print ("\ni =", a * 100 / (b * c), "(%)")
                except OverflowError:
                        print ("\nPor favor, caro usuário. Não insira valores estrondosos, pois excede o limite de caracteres suportado ;)")

            # Continuar/Voltar/Sair:

            print ("\nDesejas: \n\n1) Continuar \n2) Voltar ao menu de opções \n3) Sair")
            b = input ("\n")
            while b != "1" and b != "2" and b != "3":
                print ("*alternativa inválida*")
                print ("Desejas: \n\n1) Continuar \n2) Voltar ao menu de opções \n3) Sair")
                b = input ("\n")
            if b == "3" or b == "2":                        
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
                a = float(a)
                break
            except ValueError or TypeError:
                print ("Entre com um número!")
        if a == "s" or a == "m":            
            break
        while True:
            try:
                b = input ("Capital (C): ")
                if b == "s" or b == "m":
                    break
                b = float(b)
                break
            except ValueError or TypeError:
                print ("Entre com um número!")
        if b == "s" or b == "m":                
            break
        while True:
            try:
                c = input ("Taxa percentual (i): ")
                if c == "s" or c == "m":
                    break
                c = float(c)
                break
            except ValueError or TypeError:
                print ("Entre com um número!")
        if c == "s" or c == "m":                    
            break

        # Cálculo/Resultado:
        if c == 0 and a > 0:
            print ("\nNão me faça rir. Aplicar uma taxa de 0% e o dinheiro ter rendido alguma coisa é história para boi dormir... Perdão! Quase peguei no sono... Não, pera!")
        elif c == 0 and a == 0:
            print ("\nhmmmm... aposto que alguma vez alguém já te disse que na programação ou na matemática tudo há de ser certo, que não existe 'talvez'...\nBem, aqui está um caso bastante peculiar. Eu afirmo-te asseguradamente que não existe um valor certo para o tempo desta aplicação, qualquer valor confere. \nEla pode durar uma eternidade, até o palmeiras conquistar o mundial. Ou ela pode durar menos que 1/10000 de um segundo... \nAcredito que neste cenário é recorrente a teoria de relatividade geral de Albert Einstein; ou melhor, os aspectos mais intrínsecos do comportamento das partículas dentro do campo da mecânica quântica: \nnão há um parâmetro concreto para a posição de uma partícula, o que há é uma nuvem das possíveis possibiladades que aquela partícula pode assumir. \nMas aqui o caso é um pouco diferente: esta nuvem assume valores infinitos! É como pensar na totalidade do universo! Opss... espera! Esqueci de tomar os remédios...")

        elif a < 0 or b < 0 or c < 0:
            print ("\nNão seja assim, amigo, é vergonhoso aplicar valores negativos neste contexto...")
        else:
            try:
                print ("\nt =", a * 100 / (b * c), "mes(es)")
            except OverflowError:
                    print ("\nPor favor, caro usuário. Não insira valores estrondosos, pois excede o limite de caracteres suportado ;)")

        # Continuar/Voltar/Sair:

        print ("\nDesejas: \n\n1) Continuar \n2) Voltar ao menu de opções \n3) Sair\n")
        b = input ()
        while b != "1" and b != "2" and b != "3":
            print ("*alternativa inválida*")
            print ("Desejas: \n\n1) Continuar \n2) Voltar ao menu de opções \n3) Sair")
            b = input ("\n")
        if b == "3" or b == "2":                        
            break
        elif b == "1":
            a = "4"
print ("Adeus!")