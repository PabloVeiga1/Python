import random
n = int(input('Digite um numero'))
num_escolhido = random.randint(0,5)
if n == num_escolhido:
    print('Parabens, voce acertou!')
else:
    print('Dessa vez, eu ganhei!, o numero era {}'.format(num_escolhido))