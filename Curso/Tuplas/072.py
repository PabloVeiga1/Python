extenso = ('zero','um','dois','tres','quatro','cinco'
           ,'seis','sete','oito','nove','dez',
           'onze','doze','treze','quatorze','quinze',
           'desesseis','desessete','dezoito','dezenove','vinte')

usuario = int(input('Digite um numero entre 0 e 20: '))

while usuario not in range(0,21):
    usuario = int(input('Tente novamente.Digite um numero entre 0 e 20: '))
print(f'Voce digitou o numero {extenso[usuario]}')