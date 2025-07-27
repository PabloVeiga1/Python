import random

numeros = (random.randint(0,20),
           random.randint(0,20),
           random.randint(0,20),
           random.randint(0,20),
           random.randint(0,20))
print(f'Os numeros sorteados foram: {numeros}')
print(f'O maior valor sorteado foi {max(numeros)}')
print(f'O menor valor sorteado foi {min(numeros)}')

