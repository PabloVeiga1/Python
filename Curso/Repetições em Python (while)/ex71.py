print('='*30)
print('BANCO CEV')
print('='*30)

valor = int(input('Qual valor você quer sacar? R$ '))
total = valor
ced = 50 #Percebi que sempre devo atriuir um valor inicial e mudar dentro do WHILE
totced = 0
while True:
    if total >= ced:
        total -=ced
        totced +=1
    else:
        if totced >0:
            print(f'Total de {totced} cedulas de R$ {ced}')
            totced = 0
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
    if total == 0:
        break






