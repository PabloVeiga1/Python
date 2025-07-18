from datetime import date
#ano de nascimento
ano = int(input('Ano de nascimento:'))
#dados
idade = date.today().year - ano
print(f'Quem nasceu em {ano} tem {idade} anos em {date.today().year}')
#condicionais
if idade <18:
    print('Ainda faltam {} anos para o seu alistamento.'.format(18 - idade))
    print(f'O ano de seu alistamento sera {date.today().year + (18 - idade)}')
elif idade == 18:
    print('Voce ja tem 18 anos e deve se alistar(Caso nao tenha feito) ainda esse ano')
elif idade > 18:
    print(f'Voce ja deveria ter se alistado a {idade - 18} anos, em {date.today().year + (18 - idade)}. ')

