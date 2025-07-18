peso = float(input('Digite o seu peso [KG]: '))

altura = float(input('Digite sua altura [m]: '))

imc = peso / (altura * altura)

print(f'O IMC dessa pessoa e de: {imc:.2f}')

if imc < 18.5:
    print('Voce esta ABAIXO DO PESO!')
elif imc >= 18.5 and imc < 25:
    print('Voce esta com PESO IDEAL!')
elif imc >= 25 and imc < 30:
    print('Voce esta com SOBREPESO!')
elif imc >= 30 and imc < 40:
    print('Voce esta com OBESIDADE!')
elif imc >= 40:
    print('Voce esta com OBESIDADE MORBIDA!')
