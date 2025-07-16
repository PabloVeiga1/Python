print('=-'*20)
print('LOJA SUPER BARATAO')
print('=-'*20)

total = menor_preco = mais_mil = 0
mais_barato = ''
primeira_vez = True

while True:
    nome = str(input('Nome do produto: '))
    valor = float(input('Preço: R$ '))
    total += valor

    if primeira_vez or valor < menor_preco:
        menor_preco = valor
        mais_barato = nome
        primeira_vez = False

    if valor > 1000:
        mais_mil += 1

    continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()
    if continuar == 'N':
        print('-'*10, end='')
        print('FIM DO PROGRAMA', end='')
        print('-'*10)
        print(f'\nTotal da compra foi R$ {total:.2f}')
        print(f'Temos {mais_mil} produto(s) custando mais de R$ 1000.00')
        print(f'O produto mais barato foi {mais_barato} que custa R$ {menor_preco:.2f}')
        break
