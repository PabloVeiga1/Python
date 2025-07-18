import time
valor1 = int(input('Digite o primeiro valor: '))
valor2 = int(input('Digite o segundo valor: '))
print('=-'*10)
print('[ 1 ] somar')
print('[ 2 ] multiplicar')
print('[ 3 ] maior')
print('[ 4 ] novos numeros')
print('[ 5 ] sair do programa')
opcao = int(input('>>>>>>>> Qual a sua opcao? '))
print('=-'*10)
while opcao != 5:
    if opcao == 1:
        print(f'O resultado de {valor1} + {valor2} é {valor1 + valor2}')
    elif opcao == 2:
        print(f'O resultado de {valor1} x {valor2} é {valor1 * valor2}')
    elif opcao == 3:
        if valor1 > valor2:
            print(f'{valor1} é maior que {valor2}')
        elif valor1 < valor2:
            print(f'{valor2} é maior que {valor1}')
    elif opcao == 4:
        valor1 = int(input('Digite o primeiro valor: '))
        valor2 = int(input('Digite o segundo valor: '))
    print('=-' * 10)
    print('[ 1 ] somar')
    print('[ 2 ] multiplicar')
    print('[ 3 ] maior')
    print('[ 4 ] novos numeros')
    print('[ 5 ] sair do programa')
    opcao = int(input('>>>>>>>> Qual a sua opcao? '))
    print('=-' * 10)
if opcao == 5:
    print('Finalizando...')
    time.sleep(2)
    print('Obrigado.')
    print('=-'*10)



