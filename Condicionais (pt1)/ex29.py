v = int(input('Qual a velocidade atual do carro?'))
multa = (v - 80) * 7
if v <=80:
    print('Tenha um bom dia! Dirija com segurança!')
else:
    print('MULTADO! Voce excedeu o limite permitido que eh de 80 km/h ')
    print( f'Voce deve pagar uma multa de R${multa:.2f}!')
    print('Tenha um bom dia! Dirija com segurança!')