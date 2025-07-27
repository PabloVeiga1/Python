print('_'*40)
print(f'{"LISTAGEM DE PRECOS":^40}')
print('_'*40)
listagem = ('Pao',1,'Borracha',1.50,'Multiuso',3.50,'Frango',10.90)
for n in range(0,len(listagem),2):
    print(f'{listagem[n]:.<30}',end='')
    print(f'R${listagem[n+1]:>7.2f}')
print('_'*40)
