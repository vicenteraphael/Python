print ("\nBem-vindo(a) à Calculadora de Progressão Aritmética do Raphael\n")

ans = None
def readline(var, text):
    while True:
        try:
            var = input(text)
            if var != "s" and var != "m":
                var = float(var)
            return var
        except:
            print ("Entre com um número!")

def whole_sequence():
    first_term, last_term, ratio = None, None, None
    #Entrada
    first_term = readline(first_term, "1º termo da progressão (a1): ")
    if first_term == "s":
        return 0
    elif first_term == "m":
        return 1
    last_term = readline(last_term, "Último termo da progressão (an): ")
    if last_term == "s":
        return 0
    elif last_term == "m":
        return 1
    ratio = readline(ratio, "Razão da progressão (r): ")
    if ratio == "s":
        return 0
    elif ratio == "m":
        return 1

    # Saída:
    print ("\nTodos os termos: ")
    while first_term < last_term-2*ratio:
        print ("{}, ".format(first_term), end='')
        first_term += ratio
    print ("{} e {}\n".format(first_term+ratio, last_term))

def find_term():
    first_term, ratio, index = None, None, None
    #Entrada
    first_term =  readline(first_term, "1º termo da progressão (a1): ")
    if first_term == "s":
        return 0
    elif first_term == "m":
        return 1
    ratio =  readline(ratio, "Razão da progressão (r): ")
    if ratio == "s":
        return 0
    elif ratio == "m":
        return 1
    index = readline("Índice do termo desejado (n de an): ")
    if index == "s":
        return 0
    elif index == "m":
        return 1

    # Saída:
    print ("\nan =", first_term + (index - 1) * ratio, "\n")

def find_ratio():
    first_term, second_term = None, None
    first_term = input (first_term, "1º termo: ")
    if first_term == "s":
        return 0
    elif first_term == "m":
        return 1
    second_term = readline(second_term, "2º termo: ")
    if second_term == "s":
        return 0
    elif second_term == "m":
        return 1

    # Saída:
    print ("\nr =", second_term - first_term, "\n")

def general_sum():
    first_term, last_term, last_index = None, None, None
    #Entrada
    first_term = readline (first_term, "1º termo da progressão (a1): ")
    if first_term == "s":
        return 0
    elif first_term == "m":
        return 1
    last_term = readline(last_term, "Último termo da progressão (an): ")
    if last_term == "s":
        return 0
    elif last_term == "m":
        return 1
    last_index = input (last_index, "Índice do último termo da progressão (n de an): ")
    if last_index == "s":
        return False
    elif last_index == "m":
        return 1

    # Saída:
    print ("\nSn =", ((first_term + last_term) * last_index ) / 2)

# Menu de opções:
while ans != "s":
    print ("\nVocê deseja calcular: \n\n1) Todos os termos da progressão \n2) Um termo n da progressão (an) \n3) A razão da progressão (r) \n4) A soma geral dos termos da progressão (Sn) \n5) Sair\n")
    ans = input()
    while ans != "1" and ans != "2" and ans != "3" and ans != "4" and ans != "5" and ans != "s":
        print ("\n*alternativa inválida*")
        print ("Você deseja calcular: \n\n1) Todos os termos da progressão \n2) Um termo n da progressão (an) \n3) A razão da progressão (r) \n4) A soma geral dos termos da progressão (Sn) \n5) Sair\n")
        ans = input()
    if ans == "5" or ans == "s":
        break

    # Todos os termos da progressão:
    if ans == "1":
        print ("\n*Para sair, entre com 's'. Para voltar ao menu de opções, entre com 'm'* \nInforme-me:\n")
        while ans == "1":
            result = whole_sequence()
            if result == 0:
                ans = "s"
            elif result == 1:
                ans = None

    # Termo n da progressão (an):
    if ans == "2":
        print ("\n*Para sair, entre com 's'. Para voltar ao menu de opções, entre com 'm'* \nInforme-me:\n")
        while ans == "2":
            result = find_term()
            if result == 0:
                ans = "s"
            elif result == 1:
                ans = None

    # Razão da progressão:
    if ans == "3":
        print ("\n*Para sair, entre com 's'. Para voltar ao menu de opções, entre com 'm'*\nInforme-me dois termos consecutivos da progressão:\n")
        while ans == "3":
            result = find_ratio()
            if result == 0:
                ans = "s"
            elif result == 1:
                ans = None
    
    # Soma geral dos termos (Sn):
    if ans == "4":
        print ("\n*Para sair, entre com 's'. Para voltar ao menu de opções, entre com 'm'* \nInforme-me:\n")
        while ans == "4":
            result = general_sum()
            if result == 0:
                ans = "s"
            elif result == 1:
                ans = None

print ("\nAdeus!")