frase = input('Digite uma frase: ')
sem_espacos = frase.replace(' ','')
print(f'A frase "{frase}" possui {len(frase)} caracteres ao todo, e {len(sem_espacos)} desconsiderando os espacos')