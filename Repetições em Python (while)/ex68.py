from random import randint

valor_computador = randint(1, 10)
valor_eu = int(input('Digite um valor: '))
poi = input('Par ou Impar? [P/I] ')
cont_vitorias = 0
while True:
    if (valor_computador + valor_eu)%2 ==0 and poi == 'p':
        print(f'Voce jogou {valor_eu} e o computador {valor_computador}. Total de {valor_eu + valor_computador} DEU PAR')
        print('Voce VENCEU!')
        print('Vamos jogar novamente...')
        print('-=' * 20)
        cont_vitorias += 1
    elif (valor_computador + valor_eu)%2 !=0 and poi == 'i':
        print(f'Voce jogou {valor_eu} e o computador {valor_computador}. Total de {valor_eu + valor_computador} DEU IMPAR')
        print('Voce VENCEU!')
        print('Vamos jogar novamente...')
        print('-=' * 20)
        cont_vitorias += 1
    else:
        print('-=' * 20)
        print('Voce PERDEU!')
        print(f'Voce jogou {valor_eu} e o computador {valor_computador}.')
        print(f'Voce venceu {cont_vitorias} vezes no total')
        break
    valor_eu = int(input('Digite um valor: '))
    poi = input('Par ou Impar? [P/I] ')
