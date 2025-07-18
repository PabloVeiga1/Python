print('-'*20)
print('CADASTRE UMA PESSOA')
print('=-'*20)
#quantidades
mais_dezoito = 0
homens = 0
mulher_menos_vinte = 0

while True:
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F]: ')).upper()
    continuar = str(input('Continuar? [S/N]: ')).upper()
    if sexo == 'M':
        homens += 1
    if idade > 18:
        mais_dezoito += 1
    elif sexo == 'F' and idade < 20:
        mulher_menos_vinte+=1
    if continuar == 'N':
        print(f'Total de pessoas com mais de 18 anos: {mais_dezoito}')
        print(f'Ao todo temos {homens} homens cadastrados')
        print(f'E temos {mulher_menos_vinte} mulheres com menos de 20 anos')
        break






