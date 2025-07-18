idade_homens = []
soma_idades = 0
homem_m_velho = ''
mulher_menor_vinte = 0
for i in range(1,5):
    print('-'*5,f'{i}° PESSOA','-'*5)
    n = str(input('Nome: '))
    i = int(input('Idade: '))
    s = str(input('Sexo [M/F]: '))
    if s == 'M' and n[len(n)-1] == 'o' :
        idade_homens.append(i)
        homem_m_velho = n
    elif s == 'F' and i<20:
        mulher_menor_vinte += 1
    soma_idades += i
print(f'A media de idade do grupo eh de {soma_idades/4:.1f} anos')
print(f'O homem mais velho tem {max(idade_homens)} anos e se chama {homem_m_velho}')
print(f'Ao todo sao {mulher_menor_vinte} mulheres com menos de 20 anos.')
