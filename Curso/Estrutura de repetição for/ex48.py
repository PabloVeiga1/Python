multiplos = 0
soma = 0
for i in range (1,501,2):
    if i % 3 == 0:
        multiplos += 1
        soma += i
print(f'A soma dos {multiplos} valores solicitados eh igual a {soma}')
