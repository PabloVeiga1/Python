lista = []
for i in range(1,6):
    peso = float(input(f'Peso da {i}° pessoa: '))
    lista.append(peso)
print(f'\nO maior peso lido foi de {max(lista)}Kg\nO menor peso lido foi de {min(lista)}Kg')
