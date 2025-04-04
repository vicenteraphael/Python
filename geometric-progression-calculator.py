print ("\nBem-vindo(a) à Calculadora de Progressão Geométrica do Raphael\n")

def readline(var, text):
    while True:
        try:        
            var = input (text)
            if var != "s" and var != "m":
                var = float(var)
            return var
        except:
            print ("Entre com um número!")

def all_terms():
    firstTerm, lastTerm, ratio = None, None, None
    # Entrada:
    firstTerm = readline(firstTerm, "1º termo da progressão (a1): ")
    if firstTerm == "s":
        return 1
    elif firstTerm == "m":
        return 0
    lastTerm = readline(lastTerm, "Último termo da progressão (an): ")
    if lastTerm == "s":
        return 1
    elif lastTerm == "m":                
        return 0
    ratio = readline(ratio, "Razão da progressão (q): ")
    if ratio == "s":
        return 1
    elif ratio == "m":
        return 0

    # Saída:
    print ("\nConjunto contendo todos os termos:\n{", end=''); print (firstTerm, end='')
    firstTerm *= ratio
    while firstTerm <= lastTerm:
        print ("; {}" .format(firstTerm), end='')
        firstTerm *= ratio
    print ("}\n")

def find_general_term():
    firstTerm, index, ratio = None, None, None
    # Entrada:
    firstTerm = readline(firstTerm, "1º termo da progressão (a1): ")
    if firstTerm == "s":
        return 1
    elif firstTerm == "m":
        return 0
    index = readline(index, "Índice do termo desejado (n de an): ")
    if index == "s":
        return 1
    elif index == "m":                
        return 0
    ratio = readline(ratio, "Razão da progressão (q): ")
    if ratio == "s":
        return 1
    elif ratio == "m":
        return 0

    # Saída:
    print ("\nan =", firstTerm * ratio ** (index-1))

def find_ratio():
    anyTerm, prevTerm = None, None
    # Entrada:
    anyTerm = readline(anyTerm, "Algum termo da progressão (an): ")
    if anyTerm == "s":
        return 1
    elif anyTerm == "m":
        return 0
    prevTerm = readline(prevTerm, "Termo anterior (an - 1): ")
    if prevTerm == "s":
        return 1
    elif prevTerm == "m": 
        return 0

    # Saída:
    print ("\nq =", prevTerm / anyTerm, "\n")

def general_finite_sum():
    firstTerm, ratio, nTerms = None, None, None
    # Entrada:
    firstTerm = readline(firstTerm, "1º termo da progressão (a1): ")
    if firstTerm == "s":
        return 1
    elif firstTerm == "m":
        return 0
    ratio = readline(ratio, "Razão da progressão (q): ")
    if ratio == "s":
        return 1
    elif ratio == "m":
        return 0
    nTerms = readline(nTerms, "Quantidade de termos (n) da progressão: ")
    if nTerms == "s":
        return 1
    elif nTerms == "m":
        return 0

    # Saída:
    try:
        print ("\nSn =", (firstTerm * (ratio ** nTerms - 1)) / (ratio - 1), "\n")
    except OverflowError:
        print ("Resultado grande demais, meu nobre :/\n")

def general_infinite_sum():
    firstTerm, ratio = None, None
    # Entrada:
    firstTerm = readline(firstTerm, "1º termo da progressão (a1): ")
    if firstTerm == "s":
        return 1
    elif firstTerm == "m":
        return 0
    while True:
        ratio = readline(ratio, "Razão da progressão (q): ")
        if ratio == "s":
            return 1
        elif ratio == "m":                
            return 0         
        elif ratio <= -1 or ratio >= 1:
            print ("A razão deve estar entre 1 e -1 para que a soma infinita seja válida")
        else:
            break

    # Saída:
    print ("\ns∞ =", firstTerm / (1 - ratio), "\n")

def main(ans):
    # Menu de opções:
    while ans != "s":
        print ("Desejas calcular: \n\n1) Todos os termos da progressão \n2) Um termo n da progressão (an) \n3) A razão da progressão (q) \n4) A soma geral FINITA dos termos da progressão (Sn) \n5) A soma geral INFINITA dos termos da progressão (s∞) \n6) Sair \n")
        ans = input ()
        while ans != "1" and ans != "2" and ans != "3" and ans != "4" and ans != "5" and ans != "6" and ans != "s":
            print ("*alternativa inválida*"); print ("Desejas calcular: \n\n1) Todos os termos da progressão \n2) Um termo n da progressão (an) \n3) A razão da progressão (q) \n4) A soma geral FINITA dos termos da progressão (Sn) \n5) A soma geral INFINITA dos termos da progressão (s∞) \n6) Sair \n"); ans = input ()
        if ans == "6" or ans == "s":
            break
        
        # Todos os Termos da Progressão:
        if ans == "1":
            print ("\n*Para sair, entre com 's'. Para voltar ao menu de opções, entre com 'm'* \n\nInforme:\n")
            while ans == "1":
                result = all_terms()
                if result == 0:
                    ans = None
                elif result == 1:
                    ans = "s"

        # Termo Geral da Progressão (an):
        elif ans == "2":
            print ("\n*Para sair, entre com 's'. Para voltar ao menu de opções, entre com 'm'* \n\nInforme:\n")
            while ans == "2":
                result = find_general_term()
                if result == 0:
                    ans = None
                elif result == 1:
                    ans = "s"

        # Razão da progressão (q):
        elif ans == "3":
            print ("\n*Para sair, entre com 's'. Para voltar ao menu de opções, entre com 'm'* \n\nInforme:\n")
            while ans == "3":
                result = find_ratio()
                if result == 0:
                    ans = None
                elif result == 1:
                    ans = "s"
        
        # Soma geral FINITA dos termos da progressão (Sn):
        elif ans == "4":
            print ("\n*Para sair, entre com 's'. Para voltar ao menu de opções, entre com 'm'* \n\nInforme:\n")
            while ans == "4":
                result = general_finite_sum()
                if result == 0:
                    ans = None
                elif result == 1:
                    ans = "s"

        # Soma geral INFINITA dos termos da progressão (s∞):
        elif ans == "5":
            print ("\n*Para sair, entre com 's'. Para voltar ao menu de opções, entre com 'm'* \n\nInforme:\n")
            while ans == "5":
                result = general_infinite_sum()
                if result == 0:
                    ans = None
                elif result == 1:
                    ans = "s"

main(None)
print ("\nAdeus!")