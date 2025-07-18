salario = float(input('Digite o valor do seu salario: '))
if salario <=1250:
    novo_salario = salario + salario * 0.15
    print(f'O seu salario de R${salario} passara a ser R${novo_salario}')
else:
    novo_salario = salario + salario * 0.10
    print(f'O seu salario de R${salario} passara a ser R${novo_salario}')