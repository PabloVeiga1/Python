frase = input('Digite uma frase: ').split()
if len(frase) == 0:
    print('Voce nao digitou nenhuma palavra.')
else:
    print(f'{frase[0]} é a primeira palavra e possui {len(frase[0])} letras')
    print(f'{frase[len(frase)-1]} é última palavra e possui {len(frase[len(frase)-1])} letras')