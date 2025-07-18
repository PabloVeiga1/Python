l1 = float(input('Digite o valor do primeiro segmento:'))
l2 = float(input('Digite o valor do segundo segmento:'))
l3 = float(input('Digite o valor do terceiro segmento:'))

if l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1:
    print('Os segmentos acima PODEM formar um triangulo')
else:
    print('Os segmentos acima NAO PODEM formar um triangulo')