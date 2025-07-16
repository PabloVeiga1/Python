sexo = str(input('Informe o seu sexo: [M/F] ')).upper() #Não confundir e colocar o mesmo input aqui e dentro do while

while sexo != 'M' and sexo!= 'F':
    p2 = str(input('Dados inválidos. Por favor, informe o seu sexo: ')).upper()
    if p2 == 'M' or p2 == 'F':
        print(f'Sexo {p2} registrado com sucesso')






