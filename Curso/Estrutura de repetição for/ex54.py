from datetime import date
ano_atual = date.today().year
maiores = 0
menores = 0
for i in range(1,8):
    ano = int(input(f'Em que ano a {i}° nasceu? '))
    if ano_atual - ano >= 18:
        maiores += 1
    else:
        menores += 1
print(f'\nAo todo tivemos {maiores} maiores de idade \nE tambem tivemos {menores} menores de idade.')

