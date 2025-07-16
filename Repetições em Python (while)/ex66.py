num = int(input('Digite um numero (999 para parar): '))
soma = 0
contador = 0
while True:
    if num == 999: #A ordem aqui importa!!!!
        break
    contador += 1
    soma +=num
    num = int(input('Digite um numero (999 para parar): '))
print(f'A soma dos {contador} valores vale: {soma}')