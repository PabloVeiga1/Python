'''
len()- conta os caracteres da lista em uma string
frase.count('0') - conta quantos caracteres na string
frase.count('0',0,13) - conta quantos caracteres na string de uma posicao a outra
frase.find('deo') - procura onde comeca o trecho
'Curso' in frase - True or False

TRANSFORMACAO

frase.replace('Python','Android')
frase.upper()
frase.lower()
frase.captilize()
frase.title()
frase.strip()
frase.rstrip()
frase.lstrip()
frase.split()-Estudar por FORA
'-'.join(frase)
'''

nome = input('Digite seu nome completo: ')
print('Analisando seu nome ...')
print(f'Seu nome em maiusculas eh {nome.upper()}')
print(f'Seu nome em minusculas eh {nome.lower()}')
nome_sem_espaco = ''.join(nome.split())
print(f'Seu nome ao todo tem {len(nome_sem_espaco)} letras')
primeiro_nome = nome.split()[0]
print(f'Seu primeiro nome eh {primeiro_nome} e ele tem {len(primeiro_nome)} letras')