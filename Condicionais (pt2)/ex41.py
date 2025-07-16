from datetime import date

ano_atual = date.today().year
ano_nascimento = int(input('Ano de nascimento:'))
idade_atual = ano_atual - ano_nascimento

if idade_atual <= 9:
    print(f'O atleta tem {idade_atual} anos.')
    print('Classificacao: MIRIM')
elif idade_atual <= 14:
    print(f'O atleta tem {idade_atual} anos.')
    print('Classificacao: INFANTIL')
elif idade_atual <= 19:
    print(f'O atleta tem {idade_atual} anos.')
    print('Classificacao: JUNIOR')
elif idade_atual <= 25:
    print(f'O atleta tem {idade_atual} anos.')
    print('Classificacao: JUNIOR')
elif idade_atual > 25:
    print(f'O atleta tem {idade_atual} anos.')
    print('Classificacao: MASTER')
else:
    print('Digite uma idade valida!')
