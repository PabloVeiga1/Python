contador = 0
soma = 0

numero = int(input('Digite um numero [999 para parar]: '))

while numero != 999 :
    soma = soma + numero
    contador = contador + 1
    numero = int(input('Digite um numero [999 para parar]: '))
print(f'Voce digitou \033[32mVocê digitou {contador} numeros e a soma entre eles foi {soma}\033[0m.')