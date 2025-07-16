frase = input('Digite uma frase: ').replace(' ','').upper()
if frase == frase[::-1]:
    print(f'"{frase}" ao contrario fica:{frase[::-1]}\nTemos um palindromo!')
else:
    print(f'"{frase}" ao contrario, fica: {frase[::-1]}\nNao temos um palindromo!')

