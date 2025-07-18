continuar = 'S'
contador = 0
soma = 0
numeros = []
while continuar != 'N':
    num = int(input('Digite um numero: '))
    continuar = str(input('Quer continuar? [S/N] ')).upper()
    contador = contador + 1
    soma +=num
    numeros.append(num)
print(f'Voce digitou {contador} numeros e a media foi {soma/contador}')
print(f'O maior valor foi o {max(numeros)} e o menor foi o {min(numeros)}.')


