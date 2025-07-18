print('-'*10)
print('Sequencia de Fibonacci')
print('-'*10)
termos = int(input('Quantos termos voce quer mostrar? '))

termo1 =0
termo2 = 1
contador = 1
while contador <= termos:
    print(termo1, end='\033[31m ->\033[m ')
    termo3 = termo1 + termo2
    termo1 = termo2
    termo2 = termo3
    contador = contador + 1
print('\033[33mFim\033[m ')

