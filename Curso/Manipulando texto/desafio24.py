nome_cidade = input('Digite o nome da cidade: ')
nome_maiuscula = nome_cidade.upper()
separa_palavras = nome_maiuscula.split()
if 'SANTO' == separa_palavras[0]:
    print('Comeca')
else:
    print('Nao comeca')