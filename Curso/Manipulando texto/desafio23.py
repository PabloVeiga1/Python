num = int(input('Digite um numero de 0 a 9999: '))
print(f'Analisando o numero {num}...')
u = num // 1 %10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f'Unidade:{u}')
print(f'Dezena:{d}')
print(f'Centena:{c}')
print(f'Milhar:{m}')