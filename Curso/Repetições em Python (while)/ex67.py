
while True:
    valor = int(input('Quer ver a tabuada de qual valor? '))
    if valor <0:
        print('Programa ENCERRADO')
        break
    print('-' * 30)
    for x in range (1,11):
        print(f'{valor} X {x} = {valor * x}')
    print('-' * 30)
