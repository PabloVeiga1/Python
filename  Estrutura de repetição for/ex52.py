n = int(input('Digite um numero: '))
cont = 0
for i in range (1,n+1):
    if n % i == 0:
        print(f'\033[31m{i}\033[0m', end=' ')
        cont += 1
    else:
        print(f'\033[33m{i}\033[0m', end=' ')

if cont == 2:
    print(f'\nO numero {n} tem {cont} divisores, por isso ele eh PRIMO!')
elif cont > 2:
    print(f'\nO numero {n} tem {cont} divisores, por isso ele nao eh PRIMO!')