numeros = []
for i in range(0,5):
    n = int(input(f'Digite um valor para a Posição {i}: '))
    numeros.append(n)
print('-='*30)
print(f'Voce digitou os valores: {numeros}')
print(f'O maior valor digitado foi {max(numeros)} nas posições {numeros.index(max(numeros))} e',end =' ')
numeros.remove(max(numeros))
print(numeros.index(max(numeros)))
print(f'O menor valor digitado foi {min(numeros)} nas posições {numeros.index(min(numeros))}')