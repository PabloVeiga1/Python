print('Gerador de PA')
print('=-'*10)
termo1 = int(input('Primeiro termo: '))
razao = int(input('Razao da PA: '))
cont = 1
while cont <=10:
    print(termo1, end='\033[31m ->\033[0m ')
    termo1 = termo1 + razao
    cont += 1
print('\033[33m Fim\033[0m ')
print('=-'*10)



