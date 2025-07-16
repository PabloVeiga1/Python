from random import randint

print('Sou seu computador...\nAcabei de pensar em um número entre 0 e 10.\nSerá que voçê consegue adivinhar qual foi?')
num = int(input('Qual é o seu palpite? '))
sorteado = randint(0, 10)
cont = 1

while num != sorteado:
    cont += 1
    if num < sorteado:
        print('Mais... Tente novamente.')
    elif num > sorteado:
        print('Menos... Tente novamente.')
    num = int(input('Qual é o seu palpite? '))

if num == sorteado:
    print(f'Acertou com {cont} tentativas. Parabens!')




