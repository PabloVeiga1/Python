num = (int(input('Digite um numero: ')),
       int(input('Digite outro numero: ')),
       int(input('Digite mais um numero: ')),
       int(input('Digite o ultimo numero: ')))
print(f'Voce digitou os valores {num}')
print(f'O numero 9 apareceu {num.count(9)} vezes')

if 3 not in num:print(f'O valor 3 nao foi digitado nenhuma vez.')
else:print(f'O valor 3 apareceu na {num.index(3)+1} posicao')
print(f'Os numeros pares foram: ',end='')
for n in num:
    if n%2 ==0:
        print(n, end=' ')
