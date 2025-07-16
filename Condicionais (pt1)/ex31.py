km = float(input('Distancia em KM:'))
if km <= 200:
    print(f'O custo sera de R${km * 0.50:.2f}')
else:
    print(f'O custo sera de R${km * 0.45:.2f}')