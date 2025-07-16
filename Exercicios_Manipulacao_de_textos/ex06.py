palavra = input('Digite uma palavra: ')
ultima_letra = len(palavra)
if 'P' == palavra.capitalize()[0]:
        print(f'"{palavra.capitalize()}" comeca com "P"')
if 'a' == palavra.capitalize()[len(palavra)-1]:
    print(f'"{palavra.capitalize()}" termina com "a"')




