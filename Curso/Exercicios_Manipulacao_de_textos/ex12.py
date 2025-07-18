frase = input('Digite uma frase: ')
vogais = 'aAeEiIoOuU'
contador_v = 0
contador_c = 0

for letra in frase.replace(' ', ''):
    if letra.isalpha():
        if letra in vogais:
            contador_v += 1
        else:
            contador_c += 1

print(f'A frase "{frase}" possui {contador_v} vogais e {contador_c} consoantes.')
