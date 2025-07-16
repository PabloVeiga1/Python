print('Gerador de PA')
print('=-'*10)
termo1 = int(input('Primeiro termo: '))
razao = int(input('Razao da PA: '))
cont = 1
total = 0
mais = 10
while mais != 0 :
    total = total + mais
    while cont <= total:
        print(termo1, end='\033[31m ->\033[0m ')
        termo1 = termo1 + razao
        cont += 1
    print('\033[33m PAUSA\033[0m')
    mais = int(input('\nQuantos termos voce quer mostrar a mais? '))
print(f'Operacao encerrada com \033[33m {total}\033[0m termos gerados')









