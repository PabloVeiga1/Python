#pedindo um numero
num = int(input('Digite um numero inteiro:'))
#exibindo as opcoes
print('Escolha uma das opcoes abaixo')
print('[1] Binario')
print('[2] Octal')
print('[3] Hexadecimal')
opcao = int(input('Digite sua opcao: '))
#condicionais
if opcao == 1:
    print(f'{num} em binario eh igual a {bin(num)[2:]}')
elif opcao == 2:
    print(f'{num} em octal eh igual a {oct(num)[2:]}')
elif opcao == 3:
    print(f'{num} em hexadecal eh igual a {hex(num)[2:]}')
else:
    print('Opcao invalida!')